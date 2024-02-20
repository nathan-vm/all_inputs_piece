from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, time, date

class InputObject(BaseModel):
    input_1: str = Field(
        description="input_1 string required.",
        from_upstream="never",
    )
    input_2: Optional[str] = Field(
        default=None,
        description="input_1 string required.",
        from_upstream="allowed",
    )
    input_3: str = Field(
        description="input_3 string required from upstream.",
        from_upstream="always"
    )

class InputModel(BaseModel):
    input_array_string: List[str] = Field(
        default= [
            "default_1",
            "default_2",
            "default_3"
        ],
        description='Input array to be logged.',
        from_upstream="allowed"
    )
    input_array_object: List[InputObject] = Field(
        default=[],
        description='Input array object to be logged.',
        json_schema_extra={
            'from_upstream':"never"
        }
    )

class OutputModel(BaseModel):
    input_array_string: List[str] = Field(
        default= [
            "default_1",
            "default_2",
            "default_3"
        ],
        description='Input array to be logged.'
    )
    input_array_object: List[InputObject] = Field(
        default=[],
        description='Input array object to be logged.',
        from_upstream="never"
    )
