import enum
import logging
from typing import Dict
from typing import List
from typing import Optional

import attrs
import pendulum
from google.protobuf import duration_pb2
from typeguard import typechecked

from tecton_core import pipeline_common
from tecton_core import specs
from tecton_core import time_utils
from tecton_core.fco_container import FcoContainer
from tecton_core.feature_view_utils import CONTINUOUS_MODE_BATCH_INTERVAL
from tecton_core.id_helper import IdHelper
from tecton_core.online_serving_index import OnlineServingIndex
from tecton_core.schema import Schema
from tecton_core.specs import utils
from tecton_proto.args.feature_view_pb2 import OfflineFeatureStoreConfig
from tecton_proto.args.pipeline_pb2 import DataSourceNode
from tecton_proto.args.pipeline_pb2 import Pipeline
from tecton_proto.args.pipeline_pb2 import PipelineNode
from tecton_proto.common import data_source_type_pb2
from tecton_proto.common import schema_pb2
from tecton_proto.common.framework_version_pb2 import FrameworkVersion as FrameworkVersionProto
from tecton_proto.data import feature_view_pb2
from tecton_proto.data.feature_view_pb2 import OfflineStoreParams


logger = logging.getLogger(__name__)


# Create a parallel enum class since Python proto extensions do not use an enum class.
# Keep up-to-date with FrameworkVersion from tecton_proto/args/version_constraints.proto.
class FrameworkVersion(enum.Enum):
    UNSPECIFIED = FrameworkVersionProto.UNSPECIFIED
    FWV3 = FrameworkVersionProto.FWV3
    FWV5 = FrameworkVersionProto.FWV5


@attrs.define(frozen=True)
class FeatureDefinitionWrapper:
    """A container for a Feature View spec and its dependent specs, i.e. data sources, transformations, and entities."""

    fv_spec: specs.FeatureViewSpec
    fco_container: FcoContainer

    @typechecked
    def __init__(self, feature_view_spec: specs.FeatureViewSpec, fco_container: FcoContainer):
        return self.__attrs_init__(  # type: ignore
            fv_spec=feature_view_spec,
            fco_container=fco_container,
        )

    @property
    def id(self) -> str:
        return self.fv_spec.id

    @property
    def name(self) -> str:
        return self.fv_spec.name

    @property
    def is_temporal_aggregate(self) -> bool:
        return (
            isinstance(self.fv_spec, specs.MaterializedFeatureViewSpec)
            and self.fv_spec.type == specs.MaterializedFeatureViewType.TEMPORAL_AGGREGATE
        )

    @property
    def is_continuous(self) -> bool:
        return isinstance(self.fv_spec, specs.MaterializedFeatureViewSpec) and self.fv_spec.is_continuous

    @property
    def is_temporal(self) -> bool:
        return (
            isinstance(self.fv_spec, specs.MaterializedFeatureViewSpec)
            and self.fv_spec.type == specs.MaterializedFeatureViewType.TEMPORAL
        )

    @property
    def is_feature_table(self) -> bool:
        return isinstance(self.fv_spec, specs.FeatureTableSpec)

    @property
    def is_stream(self) -> bool:
        return (
            isinstance(self.fv_spec, specs.MaterializedFeatureViewSpec)
            and self.fv_spec.data_source_type == data_source_type_pb2.DataSourceType.STREAM_WITH_BATCH
        )

    @property
    def is_on_demand(self) -> bool:
        return isinstance(self.fv_spec, specs.OnDemandFeatureViewSpec)

    @property
    def is_incremental_backfill(self) -> bool:
        return isinstance(self.fv_spec, specs.MaterializedFeatureViewSpec) and self.fv_spec.incremental_backfills

    @property
    def get_feature_store_format_version(self) -> int:
        return self.fv_spec.feature_store_format_version

    @property
    def namespace_separator(self) -> str:
        if self.framework_version == FrameworkVersion.FWV5:
            return "__"
        else:
            return "."

    @property
    def framework_version(self) -> FrameworkVersion:
        return FrameworkVersion(self.fv_spec.metadata.framework_version)

    @property
    def time_key(self) -> Optional[str]:
        if isinstance(
            self.fv_spec,
            (specs.MaterializedFeatureViewSpec, specs.FeatureTableSpec),
        ):
            return self.fv_spec.timestamp_field
        else:
            return None

    @property
    def timestamp_key(self) -> Optional[str]:
        # TODO(jake): This property is a dupe with time_key.
        return self.time_key

    @property
    def join_keys(self) -> List[str]:
        return list(self.fv_spec.join_keys)

    @property
    def join_keys_schema(self) -> Schema:
        if self.is_on_demand:
            # For ODFV, we need to extract its dependent materialized FeatureViewSpec and join key override mapping to correctly build the spine schema.
            all_fv_nodes = pipeline_common.get_all_feature_view_nodes(self.pipeline)
            dependent_fv_specs = [
                self.fco_container.get_by_id_proto(node.feature_view_node.feature_view_id) for node in all_fv_nodes
            ]
            jk_overrides = [
                [
                    utils.JoinKeyMappingSpec(
                        spine_column_name=override_join_key.spine_column,
                        feature_view_column_name=override_join_key.feature_column,
                    )
                    for override_join_key in node.feature_view_node.feature_view.override_join_keys
                ]
                for node in all_fv_nodes
            ]
            return self.fv_spec.join_key_schema(zip(dependent_fv_specs, jk_overrides))
        else:
            return self.fv_spec.join_key_schema()

    @property
    def online_serving_index(self) -> OnlineServingIndex:
        return OnlineServingIndex(list(self.fv_spec.online_serving_keys))

    @property
    def wildcard_join_key(self) -> Optional[str]:
        """
        Returns a wildcard join key column name for the feature view if it exists;
        Otherwise returns None.
        """
        online_serving_index = self.online_serving_index
        wildcard_keys = [join_key for join_key in self.join_keys if join_key not in online_serving_index.join_keys]
        return wildcard_keys[0] if wildcard_keys else None

    @property
    def offline_store_config(self) -> OfflineFeatureStoreConfig:
        if isinstance(self.fv_spec, specs.OnDemandFeatureViewSpec) or self.fv_spec.offline_store is None:
            return OfflineFeatureStoreConfig()
        return self.fv_spec.offline_store

    @property
    def online_store_data_delay_seconds(self) -> int:
        return 0 if (self.is_stream or self.is_feature_table) else self.max_source_data_delay.in_seconds()

    @property
    def materialization_enabled(self) -> bool:
        return self.fv_spec.materialization_enabled

    @property
    def writes_to_offline_store(self) -> bool:
        # Brian: I think this should actually be `return self.fv_spec.materialization_enabled and self.fv_spec.offline`
        # Otherwise this indicates we write to the offline store when we don't since materialization is disabled.
        # Similarly, it should be impossible to set offine=True on a local object?
        return self.fv_spec.offline

    @property
    def writes_to_online_store(self) -> bool:
        return self.fv_spec.online

    @property
    def view_schema(self) -> Schema:
        return self.fv_spec.view_schema

    @property
    def materialization_schema(self) -> Schema:
        return self.fv_spec.materialization_schema

    @property
    def min_scheduling_interval(self) -> Optional[pendulum.Duration]:
        if self.is_temporal_aggregate:
            return self.fv_spec.slide_interval
        elif self.is_temporal:
            return self.fv_spec.batch_schedule
        else:
            return None

    @property
    def batch_materialization_schedule(self) -> pendulum.Duration:
        if not isinstance(self.fv_spec, specs.MaterializedFeatureViewSpec):
            msg = f"Feature definition with type {type(self.fv_spec)} does not have a batch_materialization_schedule."
            raise TypeError(msg)

        if self.fv_spec.batch_schedule is not None:
            return self.fv_spec.batch_schedule
        elif self.fv_spec.is_continuous:
            return time_utils.proto_to_duration(CONTINUOUS_MODE_BATCH_INTERVAL)
        elif self.fv_spec.slide_interval is not None:
            return self.fv_spec.slide_interval
        else:
            msg = "Materialized feature view must have a batch_materialization_schedule."
            raise ValueError(msg)

    @property
    def offline_store_params(self) -> Optional[OfflineStoreParams]:
        return self.fv_spec.offline_store_params

    @property
    def max_source_data_delay(self) -> pendulum.Duration:
        if not isinstance(self.fv_spec, specs.MaterializedFeatureViewSpec):
            msg = f"Feature definition with type {type(self.fv_spec)} does not have max_source_data_delay."
            raise TypeError(msg)
        return self.fv_spec.max_source_data_delay

    @property
    def materialization_start_timestamp(self) -> pendulum.datetime:
        if not isinstance(self.fv_spec, specs.MaterializedFeatureViewSpec):
            msg = f"Feature definition with type {type(self.fv_spec)} does not have a materialization_start_timestamp."
            raise TypeError(msg)

        return self.fv_spec.materialization_start_time

    @property
    def feature_start_timestamp(self) -> Optional[pendulum.datetime]:
        if not isinstance(self.fv_spec, specs.MaterializedFeatureViewSpec) or self.fv_spec.feature_start_time is None:
            return None

        return self.fv_spec.feature_start_time

    @property
    def time_range_policy(self) -> feature_view_pb2.MaterializationTimeRangePolicy:
        if isinstance(self.fv_spec, specs.OnDemandFeatureViewSpec) or self.fv_spec.time_range_policy is None:
            msg = "No materialization time range policy set for this feature view."
            raise ValueError(msg)

        return self.fv_spec.time_range_policy

    @property
    def data_source_ids(self) -> List[str]:
        if self.pipeline is None:
            return []

        nodes = pipeline_to_ds_inputs(self.pipeline).values()
        return [IdHelper.to_string(node.virtual_data_source_id) for node in nodes]

    @property
    def data_sources(self) -> List[specs.DataSourceSpec]:
        ds_ids = self.data_source_ids
        return self.fco_container.get_by_ids(ds_ids)

    def get_data_source_with_input_name(self, input_name) -> specs.DataSourceSpec:
        """Get the data source spec that uses `input_name` for the feature view transformation."""
        input_name_to_ds_id = pipeline_common.get_input_name_to_ds_id_map(self.pipeline)

        if input_name not in input_name_to_ds_id:
            msg = (
                f"Feature view '{self.name}' does not have an input data source with the parameter name '{input_name}'"
            )
            raise KeyError(msg)

        return self.fco_container.get_by_id(input_name_to_ds_id[input_name])

    @property
    def get_tile_interval(self) -> pendulum.Duration:
        if self.is_temporal_aggregate:
            return self.fv_spec.slide_interval
        elif self.is_temporal:
            return self.fv_spec.batch_schedule

        msg = "Invalid invocation on unsupported FeatureView type"
        raise ValueError(msg)

    @property
    def get_batch_schedule_for_version(self) -> int:
        return time_utils.convert_timedelta_for_version(
            self.fv_spec.batch_schedule, self.get_feature_store_format_version
        )

    @property
    def get_tile_interval_for_version(self) -> int:
        if self.is_temporal_aggregate:
            return time_utils.convert_timedelta_for_version(
                self.fv_spec.slide_interval, self.get_feature_store_format_version
            )
        elif self.is_temporal:
            return time_utils.convert_timedelta_for_version(
                self.fv_spec.batch_schedule, self.get_feature_store_format_version
            )

        msg = "Invalid invocation on unsupported FeatureView type"
        raise TypeError(msg)

    @property
    def get_aggregate_slide_interval_string(self) -> str:
        if not self.is_temporal_aggregate:
            msg = "Invalid invocation on unsupported FeatureView type"
            raise TypeError(msg)

        return self.fv_spec.slide_interval_string

    @property
    def aggregate_slide_interval(self) -> duration_pb2.Duration:
        if not self.is_temporal_aggregate:
            msg = "Invalid invocation on unsupported FeatureView type"
            raise TypeError(msg)

        duration = duration_pb2.Duration()
        duration.FromTimedelta(self.fv_spec.slide_interval)
        return duration

    @property
    def materialized_data_path(self) -> str:
        if isinstance(self.fv_spec, specs.OnDemandFeatureViewSpec) or self.fv_spec.materialized_data_path is None:
            msg = "No materialized data path available."
            raise ValueError(msg)

        return self.fv_spec.materialized_data_path

    @property
    def max_aggregation_window(self) -> Optional[int]:
        if not self.is_temporal_aggregate:
            return None

        return max(
            [feature.window for feature in self.fv_spec.aggregate_features],
            key=lambda window: window.ToSeconds(),
        )

    @property
    def transformations(self) -> List[specs.TransformationSpec]:
        if self.pipeline is None:
            return []

        transformation_ids = pipeline_to_transformation_ids(self.pipeline)
        return self.fco_container.get_by_ids(transformation_ids)

    @property
    def entities(self) -> List[specs.EntitySpec]:
        return self.fco_container.get_by_ids(self.fv_spec.entity_ids)

    @property
    def trailing_time_window_aggregation(self) -> Optional[feature_view_pb2.TrailingTimeWindowAggregation]:
        if not self.is_temporal_aggregate:
            return None

        return feature_view_pb2.TrailingTimeWindowAggregation(
            time_key=self.timestamp_key,
            is_continuous=self.fv_spec.is_continuous,
            aggregation_slide_period=self.aggregate_slide_interval,
            features=self.fv_spec.aggregate_features,
        )

    @property
    def serving_ttl(self) -> Optional[pendulum.Duration]:
        if isinstance(self.fv_spec, (specs.MaterializedFeatureViewSpec, specs.FeatureTableSpec)):
            return self.fv_spec.ttl
        else:
            return None

    @property
    def features(self) -> List[str]:
        return self.fv_spec.features

    @property
    def workspace(self) -> str:
        return self.fv_spec.workspace

    @property
    def request_context_keys(self) -> List[str]:
        rc_schema = self.request_context_schema
        if rc_schema is not None:
            return rc_schema.column_names()
        else:
            return []

    @property
    def request_context_schema(self) -> Schema:
        if self.pipeline is None:
            return Schema(schema_pb2.Schema())

        request_context = pipeline_common.find_request_context(self.pipeline.root)
        if request_context:
            return Schema(request_context.tecton_schema)
        else:
            return Schema(schema_pb2.Schema())

    # Returns the schema of the spine that can be used to query feature values. Note the actual spine user passes in
    # could contain extra columns that are not used by Tecton, and returned schema doesn't include these columns. For
    # details about how to build spine_schema for different FeatureView, see `spine_schema` method defined in
    # FeatureViewSpec and its children classes.
    @property
    def spine_schema(self) -> Schema:
        return self.join_keys_schema + self.request_context_schema

    @property
    def pipeline(self) -> Optional[Pipeline]:
        if isinstance(self.fv_spec, (specs.MaterializedFeatureViewSpec, specs.OnDemandFeatureViewSpec)):
            return self.fv_spec.pipeline
        else:
            # Feature Tables do not have pipelines.
            return None


def pipeline_to_ds_inputs(pipeline: Pipeline) -> Dict[str, DataSourceNode]:
    ds_nodes: Dict[str, DataSourceNode] = {}

    def _recurse_pipeline_to_ds_nodes(pipeline_node: PipelineNode, ds_nodes_: Dict[str, DataSourceNode]):
        if pipeline_node.HasField("data_source_node"):
            ds_nodes_[pipeline_node.data_source_node.input_name] = pipeline_node.data_source_node
        elif pipeline_node.HasField("transformation_node"):
            inputs = pipeline_node.transformation_node.inputs
            for input_ in inputs:
                _recurse_pipeline_to_ds_nodes(input_.node, ds_nodes_)

    _recurse_pipeline_to_ds_nodes(pipeline.root, ds_nodes)

    return ds_nodes


def pipeline_to_transformation_ids(pipeline: Pipeline) -> List[str]:
    id_list: List[str] = []

    def _recurse_pipeline_to_transformation_ids(node: PipelineNode, id_list: List[str]):
        if node.HasField("transformation_node"):
            id_list.append(IdHelper.to_string(node.transformation_node.transformation_id))
            for input in node.transformation_node.inputs:
                _recurse_pipeline_to_transformation_ids(input.node, id_list)
        return id_list

    _recurse_pipeline_to_transformation_ids(pipeline.root, id_list)
    return id_list
