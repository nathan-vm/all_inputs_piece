from pydantic import BaseModel, Field
from typing import List, Optional

class InputObject(BaseModel):
    prop1: bool = Field(
        description='prop1 required boolean.',
    )
    prop2: Optional[bool] = Field(
        default=None,
        description='prop2 boolean with default=None.',
    )

class InputModel(BaseModel):
    input_boolean: bool = Field(
        description='input_boolean required boolean.'
    )
    input_boolean_optional: Optional[bool] = Field(
        default=None,
        description='Input enum with default=None.'
    )
    input_array_boolean: List[bool] = Field(
        description='Input array to be logged.'
    )
    input_array_object: List[InputObject] = Field(
        description='Input object required.'
    )

class OutputModel(BaseModel):
    input_boolean: bool = Field(
        description='input_boolean required boolean.'
    )
    input_boolean_optional: Optional[bool] = Field(
        default=None,
        description='Input enum with default=None.'
    )
    input_array_boolean: List[bool] = Field(
        description='Input array to be logged.'
    )
    input_array_object: List[InputObject] = Field(
        description='Input object required.'
    )
