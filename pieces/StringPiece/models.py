from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
from datetime import datetime, time, date

class InputEnum(str, Enum):
    option1 = "option1"
    option2 = "option2"
    option3 = "option3"

class InputObject(BaseModel):
    prop1: str = Field(
        description='prop1 required string.',
    )
    prop2: Optional[str] = Field(
        default=None,
        description='prop2 string with default=None.',
    )

class InputModel(BaseModel):
    input_string: str = Field(
        description='input_string required string.'
    )
    input_string_optional: Optional[str] = Field(
        default=None,
        description='Input enum with default=None.'
    )
    input_textarea: Optional[str] = Field(
        description='input_textarea not required string.',
        json_schema_extra={
            'widget':"textarea",
        }
    )
    input_code: str = Field(
        default="print('Hello world!')",
        description='input_code string with default.',
        json_schema_extra={
            'widget': "codeeditor",
        }
    )
    input_date: date = Field(
        default="2023-01-01",
        description='input_date string with default.'
    )
    input_time: time = Field(
        default="16:20:00",
        description='Input time to be logged.',
    )
    input_datetime: datetime = Field(
        default="2023-01-01T16:20:00",
        description='Input datetime to be logged.'
    )
 
    input_enum: InputEnum = Field(
        default=InputEnum.option1,
        description='Input enum to be logged.'
    )

    input_array_string: List[str] = Field(
        description='Input array to be logged.'
    )
    input_array_object: List[InputObject] = Field(
        description='Input object required.'
    )

class OutputModel(BaseModel):
    input_string: str = Field(
        description='input_string required string.'
    )
    input_string_optional: Optional[str] = Field(
        default=None,
        description='Input enum with default=None.'
    )
    input_textarea: Optional[str] = Field(
        description='input_textarea not required string.',
        json_schema_extra={
            'widget':"textarea",
        }
    )
    input_code: str = Field(
        default="print('Hello world!')",
        description='input_code string with default.',
        json_schema_extra={
            'widget': "codeeditor",
        }
    )
    input_date: date = Field(
        default="2023-01-01",
        description='input_date string with default.'
    )
    input_time: time = Field(
        default="16:20:00",
        description='Input time to be logged.',
    )
    input_datetime: datetime = Field(
        default="2023-01-01T16:20:00",
        description='Input datetime to be logged.'
    )
 
    input_enum: InputEnum = Field(
        default=InputEnum.option1,
        description='Input enum to be logged.'
    )

    input_array_string: List[str] = Field(
        description='Input array to be logged.'
    )
    input_array_object: List[InputObject] = Field(
        description='Input object required.'
    )
