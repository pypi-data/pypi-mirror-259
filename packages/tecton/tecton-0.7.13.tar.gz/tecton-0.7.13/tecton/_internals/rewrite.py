from typing import Dict
from typing import List
from typing import Optional
from typing import Type

import attrs
import pendulum

from tecton._internals import time_utils
from tecton_core import conf
from tecton_core.pipeline_common import get_time_window_from_data_source_node
from tecton_core.query.node_interface import NodeRef
from tecton_core.query.node_interface import QueryNode
from tecton_core.query.nodes import AddAnchorTimeNode
from tecton_core.query.nodes import AddDurationNode
from tecton_core.query.nodes import AddEffectiveTimestampNode
from tecton_core.query.nodes import AsofJoinFullAggNode
from tecton_core.query.nodes import AsofJoinNode
from tecton_core.query.nodes import DataSourceScanNode
from tecton_core.query.nodes import EntityFilterNode
from tecton_core.query.nodes import FeatureTimeFilterNode
from tecton_core.query.nodes import FeatureViewPipelineNode
from tecton_core.query.nodes import MockDataSourceScanNode
from tecton_core.query.nodes import OfflineStoreScanNode
from tecton_core.query.nodes import PartialAggNode
from tecton_core.query.nodes import RenameColsNode
from tecton_core.query.nodes import RespectFeatureStartTimeNode
from tecton_core.query.nodes import SelectDistinctNode
from tecton_core.query.nodes import UserSpecifiedDataNode
from tecton_core.query.rewrite import Rewrite
from tecton_core.query.rewrite import tree_contains


def _find_all_nodes_of_type(tree: NodeRef, node_type: Type[QueryNode]) -> List[NodeRef]:
    """Returns a list of all NodeRefs of the given type."""
    nodes = []

    if isinstance(tree.node, node_type):
        nodes.append(tree)

    for subtree in tree.inputs:
        nodes.extend(_find_all_nodes_of_type(subtree, node_type))

    return nodes


class MockDataRewrite(Rewrite):
    """
    Replace DataSourceScanNode with MockDataSourceScanNode based on DataSource ID map.
    """

    def __init__(self, mock_data: Dict[str, NodeRef]):
        self.mock_data = mock_data

    def rewrite(self, tree: NodeRef):
        if isinstance(tree.node, DataSourceScanNode):
            node = tree.node
            if node.ds.id in self.mock_data:
                # Replace with mock data
                tree.node = MockDataSourceScanNode(
                    self.mock_data[node.ds.id],
                    node.ds,
                    self.mock_data[node.ds.id].columns,
                    node.start_time,
                    node.end_time,
                )
        else:
            for i in tree.inputs:
                self.rewrite(i)


class SpineEntityPushdown(Rewrite):
    """Filters the original feature data with respect to the entities contained in a spine.

    This should be applied to AsofJoinNodes and AsofJoinFullAggNodes since both of have sorts (as part of windows), for
    which we would like to minimize memory usage.
    """

    def __init__(self):
        pass

    def rewrite(self, tree: NodeRef):
        if isinstance(tree.node, AsofJoinNode):
            self.rewrite_asof(tree)
        elif isinstance(tree.node, AsofJoinFullAggNode):
            self.rewrite_asof_full_agg(tree)
        else:
            for i in tree.inputs:
                self.rewrite(i)

    def rewrite_asof(self, tree: NodeRef):
        node = tree.node
        # In our current usage of AsofJoinNode, we always pass in the spine on the left.
        spine_df = NodeRef.shallow_copy(node.left_container.node)
        self.pushdown_entities(node.right_container.node, spine_df, node.join_cols)

    def rewrite_asof_full_agg(self, tree: NodeRef):
        node = tree.node

        # We only want to rewrite for a user specified spine.
        if not tree_contains(node.spine, UserSpecifiedDataNode):
            return
        spine = NodeRef.shallow_copy(node.spine)
        self.pushdown_entities(node.partial_agg_node, spine, node.fdw.join_keys)

    def pushdown_entities(self, tree: NodeRef, spine: NodeRef, join_cols: List[str]):
        node = tree.node
        can_be_pushed_down = (
            RespectFeatureStartTimeNode,
            RenameColsNode,
            FeatureTimeFilterNode,
            AddAnchorTimeNode,
            AddDurationNode,
            AddEffectiveTimestampNode,
            PartialAggNode,
        )
        if isinstance(node, can_be_pushed_down):
            self.pushdown_entities(node.input_node, spine, join_cols)
        else:
            entities_node = SelectDistinctNode(spine, join_cols).as_ref()
            tree.node = EntityFilterNode(node.as_ref(), entities_node, join_cols)


class SpineTimePushdown(Rewrite):
    """
    Adds time filter ranges based on the time limits of the spine.

    For example, if the spine in a fv.ghf() has time range [start, end], then the rewrite might apply that time range
    as a filter to any FeatureViewPipelineNodes, OfflineStoreScanNodes, or DataSourceScanNodes that are part of the
    feature data (with the appropriate modifications to the time range to account for factors such as batch schedule,
    data delay, etc.).
    """

    def __init__(self):
        # The spine time limits are the same for all spines used throughout the query, so we only calculate once.
        self.spine_time_limits: Optional[pendulum.Period] = None

    def rewrite(self, tree: NodeRef):
        if isinstance(tree.node, AsofJoinNode):
            self.rewrite_asof(tree)
        elif isinstance(tree.node, AsofJoinFullAggNode):
            self.rewrite_asof_full_agg(tree)
        else:
            for i in tree.inputs:
                self.rewrite(i)

    def rewrite_asof(self, tree: NodeRef):
        node = tree.node
        # In our current usage of the code, we always pass in the spine on the left side of the asof join.
        # This rewrite is still applicable for any type of dataframe on the left, but referring to it as spine
        # to make the naming match up with the aggregate case (in which the spine is not on the left).
        if self.spine_time_limits is None:
            cur_node = node.left_container.node.node
            self.spine_time_limits = _get_spine_time_limits(cur_node)

        self.pushdown_time_range(node.right_container.node, self.spine_time_limits)

    def rewrite_asof_full_agg(self, tree: NodeRef):
        """Computes the spine time limits and pushes them down to all relevant nodes in the partial aggregates."""
        node = tree.node

        # For an AsofFullAggJoinNode, the spine is the left side of the join and the partial aggregates are the right.
        # The rewrite should only be applied when (a) the correct time range can be determined from the spine and (b)
        # specific time filters have not yet been applied to the partial aggregates.
        # Condition (a) means that the spine must contain a UserSpecifiedDataNode.
        # Condition (b) means that the fv.run and fv.ghf(time range) cases should be avoided, since the time ranges will
        # already have been applied to the partial aggregates. Both of these cases use a PartialAggNode as a fake spine,
        # so they can be avoided by skipping the rewrite if the spine contains a PartialAggNode.
        if tree_contains(node.spine, PartialAggNode) or not tree_contains(node.spine, UserSpecifiedDataNode):
            return

        if self.spine_time_limits is None:
            self.spine_time_limits = _get_spine_time_limits(node)
        self.pushdown_time_range(node.partial_agg_node, self.spine_time_limits)

    # Push down and convert spine time filter to either raw data or feature time filter at the DataSourceScanNode or OfflineStoreScanNode.
    # Nodes that do not affect the correlation with the spine time range are enumerated in the can_be_pushed_down list.
    def pushdown_time_range(self, tree: NodeRef, spine_time_limits: pendulum.Period):
        node = tree.node
        can_be_pushed_down = (
            RespectFeatureStartTimeNode,
            RenameColsNode,
            PartialAggNode,
            FeatureTimeFilterNode,
            AddAnchorTimeNode,
            AddDurationNode,
            AddEffectiveTimestampNode,
        )
        if isinstance(node, can_be_pushed_down):
            self.pushdown_time_range(node.input_node, spine_time_limits)
        elif isinstance(node, (OfflineStoreScanNode, FeatureViewPipelineNode)):
            feature_time_limits = time_utils.get_feature_data_time_limits(
                fd=node.feature_definition_wrapper, spine_time_limits=spine_time_limits
            )
            if isinstance(node, FeatureViewPipelineNode):
                # swap the pipeline node to add new time limits
                node = FeatureViewPipelineNode(node.inputs_map, node.feature_definition_wrapper, feature_time_limits)
                tree.node = node

                for n in node.inputs:
                    if isinstance(n.node, DataSourceScanNode):
                        # this method will convert aligned_feature_time_limits to raw data time limits by accounting for FilteredSource offsets etc.
                        data_time_filter = get_time_window_from_data_source_node(
                            feature_time_limits,
                            node.feature_definition_wrapper.batch_materialization_schedule,
                            n.node.ds_node,
                        )
                        if data_time_filter is not None:
                            n.node = attrs.evolve(
                                n.node, start_time=data_time_filter.start, end_time=data_time_filter.end
                            )
            elif isinstance(node, OfflineStoreScanNode):
                tree.node = attrs.evolve(node, partition_time_filter=feature_time_limits)


# Mutates the input
def rewrite_tree_for_spine(tree: NodeRef):
    if not conf.get_bool("QUERY_REWRITE_ENABLED"):
        return
    rewrites = [SpineTimePushdown(), SpineEntityPushdown()]
    for rewrite in rewrites:
        rewrite.rewrite(tree)


def _get_spine_user_specified_data_node(cur_node: QueryNode) -> Optional[UserSpecifiedDataNode]:
    if isinstance(cur_node, UserSpecifiedDataNode):
        return cur_node

    # UserSpecifiedDataNode can be nested inside a spine subtree.
    # eg. The spine can be a SelectDistinctNode -> UserSpecifiedNode
    for child in cur_node.inputs:
        node = _get_spine_user_specified_data_node(child.node)
        if node:
            return node
    return None


def _get_spine_time_limits(cur_node: QueryNode) -> Optional[pendulum.Period]:
    user_specified_data_node = _get_spine_user_specified_data_node(cur_node)
    if not user_specified_data_node:
        return None
    timestamp_key = user_specified_data_node.metadata["timestamp_key"]
    return user_specified_data_node.data.get_time_range(timestamp_key)
