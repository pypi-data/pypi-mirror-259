from collections import namedtuple
from enum import Enum
from typing import List
from typing import Union

from pyspark.sql import types as spark_types
from typeguard import typechecked

from tecton_core import data_types as tecton_types


class DataType(namedtuple("DataType", ["name", "spark_type", "tecton_type"]), Enum):
    Int64 = "Int64", spark_types.LongType(), tecton_types.Int64Type()
    Float32 = "Float32", spark_types.FloatType(), tecton_types.Float32Type()
    Float64 = "Float64", spark_types.DoubleType(), tecton_types.Float64Type()
    String = "String", spark_types.StringType(), tecton_types.StringType()
    Bool = "Bool", spark_types.BooleanType(), tecton_types.BoolType()
    Timestamp = "Timestamp", spark_types.TimestampType(), tecton_types.TimestampType()

    def __repr__(self):
        return self.name


class Array:
    def __init__(self, element_type: Union[DataType, "Array", "Struct", "Map"]):
        self.element_type = element_type

    @property
    def spark_type(self) -> spark_types.ArrayType:
        return spark_types.ArrayType(self.element_type.spark_type)

    @property
    def tecton_type(self) -> tecton_types.ArrayType:
        return tecton_types.ArrayType(self.element_type.tecton_type)

    def __repr__(self):
        return f"Array({repr(self.element_type)})"


Int64 = DataType.Int64
Float32 = DataType.Float32
Float64 = DataType.Float64
String = DataType.String
Bool = DataType.Bool
Timestamp = DataType.Timestamp


@typechecked
class Field:
    def __init__(
        self,
        name: str,
        dtype: Union[DataType, Array, "Struct", "Map"],
    ):
        self.name = name
        self.dtype = dtype

    def spark_type(self) -> spark_types.StructField:
        return spark_types.StructField(self.name, self.dtype.spark_type)

    def tecton_type(self) -> tecton_types.StructField:
        return tecton_types.StructField(self.name, self.dtype.tecton_type)

    def __repr__(self):
        return f"Field('{self.name}', {repr(self.dtype)})"


@typechecked
class Struct:
    def __init__(self, fields: List[Field]):
        self.fields = fields

    @property
    def spark_type(self) -> spark_types.StructType:
        spark_fields = [field.spark_type() for field in self.fields]
        return spark_types.StructType(spark_fields)

    @property
    def tecton_type(self) -> tecton_types.StructType:
        struct_fields = [field.tecton_type() for field in self.fields]
        return tecton_types.StructType(struct_fields)

    def __repr__(self):
        return f"Struct({self.fields})"


@typechecked
class Map:
    # key_type only allows String as of 07/07/2023. From type annotations perspective, we allow all types to be passed
    # in here so users could receive better error message from MDS instead of python type checking error.
    def __init__(
        self, key_type: Union[DataType, Array, Struct, "Map"], value_type: Union[DataType, Array, Struct, "Map"]
    ):
        self.key_type = key_type
        self.value_type = value_type

    @property
    def spark_type(self) -> spark_types.MapType:
        return spark_types.MapType(self.key_type.spark_type, self.value_type.spark_type)

    @property
    def tecton_type(self) -> tecton_types.MapType:
        return tecton_types.MapType(self.key_type.tecton_type, self.value_type.tecton_type)

    def __repr__(self):
        return f"Map({repr(self.key_type)}, {repr(self.value_type)})"
