from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional

class InputEnum(float, Enum):
    option1 = 1.0
    option2 = 2.0
    option3 = 3.0

class InputObject(BaseModel):
    prop1: float = Field(
        description='prop1 required float.',
    )
    prop2: Optional[float] = Field(
        default=None,
        description='prop2 float with default=None.',
    )

class InputModel(BaseModel):
    input_float: float = Field(
        description='Input float required.'
    )
    input_float_optional: Optional[float] = Field(
        default=None,
        description='Input float with default=None.'
    )
    input_enum: InputEnum = Field(
        default=InputEnum.option1,
        description='Input enum with default.'
    )
    input_array_float: List[float] = Field(
        description='Input array.'
    )
    input_array_object: List[InputObject] = Field(
        description='Input object required.'
    )

class OutputModel(BaseModel):
    input_float: float = Field(
        description='input_float required float.'
    )
    input_float_optional: Optional[float] = Field(
        default=None,
        description='Input enum with default=None.'
    )
    input_enum: InputEnum = Field(
        default=InputEnum.option1,
        description='Input enum.'
    )
    input_array_float: List[float] = Field(
        description='Input array.'
    )
    input_array_object: List[InputObject] = Field(
        description='Input object required.'
    )
