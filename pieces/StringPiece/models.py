from pydantic import BaseModel, Field
from typing import Optional

class InputModel(BaseModel):
    input_string: str = Field(
        description='Input string required.'
    )
    input_string_optional: Optional[str] = Field(
        default=None,
        description='Input string with default=None.'
    )
    input_textarea: Optional[str] = Field(
        default="Lorem ipsum",
        description='input_textarea not required string.',
        json_schema_extra={
            'widget':"textarea",
        }
    )
    input_code: str = Field(
        description='input_code string with default.',
        json_schema_extra={
            'widget': "codeeditor",
        }
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
