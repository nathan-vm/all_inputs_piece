from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional

class InputEnum(int, Enum):
    option1 = 1
    option2 = 2
    option3 = 3

class InputObject(BaseModel):
    prop1: int = Field(
        description='prop1 required integer.',
    )
    prop2: Optional[int] = Field(
        default=None,
        description='prop2 integer with default=None.',
    )

class InputModel(BaseModel):
    input_integer: int = Field(
        description='input_integer required integer.'
    )
    input_integer_optional: Optional[int] = Field(
        default=None,
        description='Input enum with default=None.'
    )
    input_enum: InputEnum = Field(
        default=InputEnum.option1,
        description='Input enum to be logged.'
    )
    input_array_integer: List[int] = Field(
        description='Input array to be logged.'
    )
    input_array_object: List[InputObject] = Field(
        description='Input object required.'
    )

class OutputModel(BaseModel):
    input_integer: int = Field(
        description='input_integer required integer.'
    )
    input_integer_optional: Optional[int] = Field(
        default=None,
        description='Input enum with default=None.'
    )
    input_enum: InputEnum = Field(
        default=InputEnum.option1,
        description='Input enum to be logged.'
    )
    input_array_integer: List[int] = Field(
        description='Input array to be logged.'
    )
    input_array_object: List[InputObject] = Field(
        description='Input object required.'
    )
