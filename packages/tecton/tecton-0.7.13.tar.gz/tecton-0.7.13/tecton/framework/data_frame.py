import logging
import time
import typing
from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import attr
import numpy
import pandas
import pyspark
import pytz

from tecton import snowflake_context
from tecton._internals.data_frame_helper import _get_time_limits_of_dataframe
from tecton._internals.rewrite import rewrite_tree_for_spine
from tecton._internals.sdk_decorators import sdk_public_method
from tecton._internals.utils import get_time_limits_of_pandas_dataframe
from tecton_athena import athena_session
from tecton_athena.data_catalog_helper import register_feature_view_as_athena_table_if_necessary
from tecton_athena.query.translate import AthenaSqlExecutor
from tecton_athena.query.translate import athena_convert
from tecton_core import conf
from tecton_core import data_types
from tecton_core.query.node_interface import DataframeWrapper
from tecton_core.query.node_interface import NodeRef
from tecton_core.query.node_interface import recurse_query_tree
from tecton_core.query.nodes import MultiOdfvPipelineNode
from tecton_core.query.nodes import OfflineStoreScanNode
from tecton_core.query.nodes import RenameColsNode
from tecton_core.query.nodes import UserSpecifiedDataNode
from tecton_core.query.rewrite import tree_contains
from tecton_core.schema import Schema
from tecton_spark import schema_spark_utils
from tecton_spark.query import translate


if typing.TYPE_CHECKING:
    import snowflake.snowpark

logger = logging.getLogger(__name__)

# We have to use Any here because snowflake.snowpark.DataFrame is not a direct dependency of the SDK.
snowpark_dataframe = Any

_internal_index_column = "_tecton_internal_index_col"


def set_pandas_timezone_from_spark(pandas_df):
    """Match pandas timezone to that of Spark, s.t. the timestamps are correctly displayed."""
    from tecton.tecton_context import TectonContext

    tz = TectonContext.get_instance()._spark.conf.get("spark.sql.session.timeZone")
    for col in pandas_df.columns:
        if pandas.core.dtypes.common.is_datetime64_dtype(pandas_df[col]):
            pandas_df[col] = pandas_df[col].dt.tz_localize(pytz.timezone(tz))
            pandas_df[col] = pandas_df[col].dt.tz_convert(pytz.timezone("UTC"))
            pandas_df[col] = pandas_df[col].dt.tz_localize(None)
    return pandas_df


@attr.s(auto_attribs=True)
class FeatureVector(object):
    """
    FeatureVector Class.

    A FeatureVector is a representation of a single feature vector. Usage of a FeatureVector typically involves
    extracting the feature vector using ``to_pandas()``, ``to_dict()``, or ``to_numpy()``.

    """

    _names: List[str]
    _values: List[Union[int, str, bytes, float, list]]
    _effective_times: List[Optional[datetime]]
    slo_info: Optional[Dict[str, str]] = None

    @sdk_public_method
    def to_dict(
        self, return_effective_times: bool = False
    ) -> Dict[str, Union[int, str, bytes, float, list, dict, None]]:
        """Turns vector into a Python dict.

        :param: return_effective_times: Whether to return the effective time of the feature.

        :return: A Python dict.
        """
        if return_effective_times:
            return {
                name: {"value": self._values[i], "effective_time": self._effective_times[i]}
                for i, name in enumerate(self._names)
            }

        return dict(zip(self._names, self._values))

    @sdk_public_method
    def to_pandas(self, return_effective_times: bool = False) -> pandas.DataFrame:
        """Turns vector into a Pandas DataFrame.

        :param: return_effective_times: Whether to return the effective time of the feature as part of the DataFrame.

        :return: A Pandas DataFrame.
        """
        if return_effective_times:
            return pandas.DataFrame(
                list(zip(self._names, self._values, self._effective_times)), columns=["name", "value", "effective_time"]
            )

        return pandas.DataFrame([self._values], columns=self._names)

    @sdk_public_method
    def to_numpy(self, return_effective_times: bool = False) -> numpy.array:
        """Turns vector into a numpy array.

        :param: return_effective_times: Whether to return the effective time of the feature as part of the list.

        :return: A numpy array.
        """
        if return_effective_times:
            return numpy.array([self._values, self._effective_times])

        return numpy.array(self._values)

    def _update(self, other: "FeatureVector"):
        self._names.extend(other._names)
        self._values.extend(other._values)
        self._effective_times.extend(other._effective_times)


# NOTE: use repr=False to avoid printing out the underlying dataframes when used in REPL/notebook.
@attr.define(repr=False)
class TectonDataFrame(DataframeWrapper):
    """
    A thin wrapper around Pandas, Spark, and Snowflake dataframes.
    """

    _spark_df: Optional[pyspark.sql.DataFrame] = None
    _pandas_df: Optional[pandas.DataFrame] = None
    # TODO: Change the type to snowflake.snowpark.DataFrame, currently it will
    # fail type checking for our auto generated doc.
    _snowflake_df: Optional[Any] = None
    # should already by optimized
    _querytree: Optional[NodeRef] = attr.field(default=None, repr=lambda x: "TectonQueryTree")
    _temp_table_registered: Optional[set] = None

    # _schema is the schema of TectonDataFrame. It is present only if the TectonDataFrame is built from a pandas
    # dataframe as a spine and it is used when converting a pandas datafarme to a spark dataframe. Note the _schema only
    # contains the name and data type for those columns Tecton manages. If the spine contains extra columns like `label`
    # etc, those columns are converted to their default spark data types.
    _schema: Optional[Schema] = None

    @sdk_public_method
    def explain(
        self,
        node_id: bool = True,
        name: bool = True,
        description: bool = True,
        columns: bool = False,
    ):
        """Prints the query tree. Should only be used when this TectonDataFrame is backed by a query tree.

        Args:
            node_id: If True, the unique id associated with each node will be rendered.
            name: If True, the class names of the nodes will be rendered.
            description: If True, the actions of the nodes will be rendered.
            columns: If True, the columns of each node will be rendered as an appendix after tree itself.
        """
        if self._querytree:
            if not name and not description:
                msg = "At least one of 'name' or 'description' must be True."
                raise RuntimeError(msg)
            if columns and not node_id:
                msg = "Can only show columns if 'node_id' is True."
                raise RuntimeError(msg)
            print(self._querytree.pretty_str(node_id=node_id, name=name, description=description, columns=columns))
        else:
            print("Explain is only available for TectonDataFrames backed by a query tree.")

    @sdk_public_method
    def to_spark(self) -> pyspark.sql.DataFrame:
        """Returns data as a Spark DataFrame.

        :return: A Spark DataFrame.
        """
        if self._spark_df is not None:
            return self._spark_df
        else:
            from tecton.tecton_context import TectonContext

            tc = TectonContext.get_instance()
            if self._querytree is not None:
                return translate.spark_convert(self._querytree).to_dataframe(tc._spark)
            elif self._pandas_df is not None:
                if self._schema is not None:
                    extra_columns = list(set(self._pandas_df.columns) - set(self._schema.column_names()))
                    if len(extra_columns) == 0:
                        pdf = self._pandas_df[self._schema.column_names()]
                        return tc._spark.createDataFrame(pdf, schema=schema_spark_utils.schema_to_spark(self._schema))
                    else:
                        # If there are extra columns beyond Tecton's management sopce, it splits the spine into two
                        # parts:
                        #   1. sub_df_1, which contains Tecton managed columns, is built with explicit schema.
                        #   2. sub_df_2, which contains those extra columns, is built with spark default schema(no
                        #      explicit schema passed in.
                        # Eventually these two parts are joined together using an internal index column, which is
                        # dropped afterwards. Note the join operation isn't expensive here given it is backed by a
                        # pandas dataframe that is already loaded into memory.
                        pdf = self._pandas_df.rename_axis(_internal_index_column).reset_index()
                        pdf_schema = self._schema + Schema.from_dict({_internal_index_column: data_types.Int64Type()})
                        sub_df_1 = tc._spark.createDataFrame(
                            pdf[pdf_schema.column_names()], schema=schema_spark_utils.schema_to_spark(pdf_schema)
                        )
                        sub_df_2 = tc._spark.createDataFrame(pdf[[_internal_index_column] + extra_columns])
                        return sub_df_1.join(sub_df_2, on=_internal_index_column).drop(_internal_index_column)
                else:
                    return tc._spark.createDataFrame(self._pandas_df)
            else:
                raise NotImplementedError

    @sdk_public_method
    def to_pandas(self) -> pandas.DataFrame:
        """Returns data as a Pandas DataFrame.

        :return: A Pandas DataFrame.
        """
        if self._pandas_df is not None:
            return self._pandas_df

        assert self._spark_df is not None or self._snowflake_df is not None or self._querytree is not None

        if self._spark_df is not None:
            return set_pandas_timezone_from_spark(self._spark_df.toPandas())

        if self._snowflake_df is not None:
            return self._snowflake_df.to_pandas(statement_params={"SF_PARTNER": "tecton-ai"})

        if self._querytree is not None:
            if conf.get_or_none("SQL_DIALECT") == "athena":
                self._register_tables()
                session = athena_session.get_session()
                recurse_query_tree(
                    self._querytree,
                    lambda node: register_feature_view_as_athena_table_if_necessary(
                        node.feature_definition_wrapper, session
                    )
                    if isinstance(node, OfflineStoreScanNode)
                    else None,
                )
                views = self._get_querytree_views()
                for view_name, view_sql in views:
                    session.create_view(view_sql, view_name)
                try:
                    athena_sql_executor = AthenaSqlExecutor(session)
                    df = athena_convert(self._querytree, athena_sql_executor).to_dataframe()
                finally:
                    # A tree and its subtree can share the same temp tables. If to_pandas() is called
                    # concurrently, tables can be deleted when they are still being used by the other tree.
                    self._drop_temp_tables()
                    for view_name, _ in views:
                        session.delete_view_if_exists(view_name)
                return df
            else:
                return set_pandas_timezone_from_spark(self.to_spark().toPandas())

    def _to_sql(self, create_temp_views: bool = False):
        if self._querytree is not None:
            # prevent registering the same spine multiple times.
            if create_temp_views:
                self._register_tables()
            if tree_contains(self._querytree, MultiOdfvPipelineNode):
                # SQL is not available for ODFVs. Showing SQL only for the subtree below the ODFV pipeline
                subtree = self.get_sql_node(self._querytree)
                return subtree.to_sql()
            else:
                return self._querytree.to_sql()
        else:
            raise NotImplementedError

    def get_sql_node(self, tree: NodeRef):
        # Returns the first node from which SQL can be generated(subtree below ODFV pipeline)
        can_be_pushed = (
            MultiOdfvPipelineNode,
            RenameColsNode,
        )
        if isinstance(tree.node, can_be_pushed):
            return self.get_sql_node(tree.node.input_node)
        return tree

    def _register_tables(self):
        self._temp_table_registered = self._temp_table_registered or set()

        def maybe_register_temp_table(node):
            if isinstance(node, UserSpecifiedDataNode):
                tmp_table_name = node.data._temp_table_name
                if tmp_table_name not in self._temp_table_registered:
                    node.data._register_temp_table()
                self._temp_table_registered.add(tmp_table_name)

        recurse_query_tree(
            self._querytree,
            maybe_register_temp_table,
        )

    def _get_querytree_views(self):
        qt_views = []
        recurse_query_tree(self._querytree, lambda node: qt_views.extend(node.get_sql_views()))
        return qt_views

    @sdk_public_method
    def to_snowflake(self) -> snowpark_dataframe:
        """
        Deprecated. Please use to_snowpark() instead.
        Returns data as a Snowflake DataFrame.

        :return: A Snowflake DataFrame.
        :meta private:
        """
        msg = "to_snowflake() is deprecated and is no longer supported in 0.7 PLease use to_snowpark() instead."
        raise RuntimeError(msg)

    @sdk_public_method
    def to_snowpark(self) -> snowpark_dataframe:
        """
        Returns data as a Snowpark DataFrame.

        :return: A Snowpark DataFrame.
        """
        if self._snowflake_df is not None:
            return self._snowflake_df

        assert self._pandas_df is not None

        from tecton.snowflake_context import SnowflakeContext

        if conf.get_bool("ALPHA_SNOWFLAKE_SNOWPARK_ENABLED"):
            return SnowflakeContext.get_instance().get_session().createDataFrame(self._pandas_df)
        else:
            msg = "to_snowpark() is only available with Snowpark enabled"
            raise Exception(msg)

    def get_time_range(self, timestamp_key):
        if conf.get_or_none("SQL_DIALECT") == "snowflake":
            raise NotImplementedError
        if conf.get_or_none("SQL_DIALECT") == "athena":
            return get_time_limits_of_pandas_dataframe(self.to_pandas(), timestamp_key)
        else:
            return _get_time_limits_of_dataframe(self.to_spark(), timestamp_key)

    @classmethod
    def _create(
        cls,
        df: Union[pyspark.sql.DataFrame, pandas.DataFrame, NodeRef],
        rewrite: bool = True,
    ):
        """Creates a Tecton DataFrame from a Spark or Pandas DataFrame."""
        if isinstance(df, pandas.DataFrame):
            return cls(spark_df=None, pandas_df=df, snowflake_df=None)
        elif isinstance(df, pyspark.sql.DataFrame):
            return cls(spark_df=df, pandas_df=None, snowflake_df=None)
        elif isinstance(df, NodeRef):
            if rewrite:
                rewrite_tree_for_spine(df)
            return cls(spark_df=None, pandas_df=None, snowflake_df=None, querytree=df)

        msg = f"DataFrame must be of type pandas.DataFrame or pyspark.sql.Dataframe, not {type(df)}"
        raise TypeError(msg)

    @classmethod
    def _create_from_pandas_with_schema(cls, df: pandas.DataFrame, schema: Schema):
        if isinstance(df, pandas.DataFrame):
            return cls(spark_df=None, pandas_df=df, snowflake_df=None, schema=schema)
        msg = f"DataFrame must be pandas.DataFrame when using _create_from_pandas, not {type(df)}"
        raise TypeError(msg)

    @classmethod
    # This should be merged into _create once snowpark is installed with pip
    def _create_with_snowflake(cls, df: "snowflake.snowpark.DataFrame"):
        """Creates a Tecton DataFrame from a Snowflake DataFrame."""
        from snowflake.snowpark import DataFrame as SnowflakeDataFrame

        if isinstance(df, SnowflakeDataFrame):
            return cls(spark_df=None, pandas_df=None, snowflake_df=df)

        msg = f"DataFrame must be of type snowflake.snowpark.Dataframe, not {type(df)}"
        raise TypeError(msg)

    def subtree(self, node_id: int) -> "TectonDataFrame":
        """Creates a TectonDataFrame from a subtree of prior querytree labeled by a node id in .explain()."""
        if not self._querytree:
            msg = "Cannot construct a TectonDataFrame from a node id."
            raise RuntimeError(msg)

        tree = self._querytree.create_tree()

        # Do not apply rewrites again as they should have already been applied when generating the query tree for this
        # TectonDataFrame.
        return TectonDataFrame._create(NodeRef(tree.get_node(node_id).data), rewrite=False)

    def _timed_to_pandas(self):
        """Convenience method for measuring performance."""
        start = time.time()
        ret = self.to_spark().toPandas()
        end = time.time()
        print(f"took {end-start} seconds")
        return ret

    # The methods below implement the DataframeWrapper interface
    def _register_temp_table(self):
        # TODO(TEC-11647): this will be merged with ALPHA_ATHENA_COMPUTE_ENABLED
        if conf.get_or_none("SQL_DIALECT") == "athena":
            session = athena_session.get_session()
            session.write_pandas(self.to_pandas(), self._temp_table_name)
        elif conf.get_or_none("SQL_DIALECT") == "snowflake":
            session = snowflake_context.SnowflakeContext.get_instance().get_session()
            session.write_pandas(
                self.to_pandas(),
                table_name=self._temp_table_name,
                auto_create_table=True,
                table_type="temporary",
                quote_identifiers=True,
                overwrite=True,
            )
        else:
            self.to_spark().createOrReplaceTempView(self._temp_table_name)

    def _drop_temp_tables(self):
        # TODO(TEC-11647): this will be merged with ALPHA_ATHENA_COMPUTE_ENABLED
        # TODO: implement cleanup using this prior to enabling athena-sql mode in tests
        if conf.get_or_none("SQL_DIALECT") == "athena":
            session = athena_session.get_session()
            if self._temp_table_registered:
                for temp_table in self._temp_table_registered:
                    session.delete_table_if_exists(session.get_database(), temp_table)
                self._temp_table_registered = None
        else:
            from tecton.tecton_context import TectonContext

            spark = TectonContext.get_instance()._spark
            spark.catalog.dropTempView(self._temp_table_name)

    def _select_distinct(self, columns: List[str]) -> DataframeWrapper:
        if self._pandas_df is not None:
            return TectonDataFrame._create(self._pandas_df[columns].drop_duplicates())
        elif self._spark_df is not None:
            return TectonDataFrame._create(self._spark_df.select(columns).distinct())
        else:
            raise NotImplementedError

    @property
    def _dataframe(self) -> Union[pyspark.sql.DataFrame, pandas.DataFrame]:
        if self._spark_df is not None:
            return self._spark_df
        elif self._pandas_df is not None:
            return self._pandas_df
        elif self._querytree:
            if conf.get_or_none("SQL_DIALECT") == "athena":
                return self.to_pandas()
            else:
                return self.to_spark()
        else:
            raise NotImplementedError

    @property
    def columns(self) -> List[str]:
        if self._querytree:
            return self._querytree.columns
        elif self._spark_df is not None:
            return self._spark_df.columns
        elif self._pandas_df is not None:
            return list(self._pandas_df.columns)
        else:
            raise NotImplementedError


# for legacy compat
DataFrame = TectonDataFrame
