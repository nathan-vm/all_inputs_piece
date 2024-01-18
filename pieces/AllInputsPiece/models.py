from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional, Union
from datetime import datetime, time, date
from annotated_types import Gt
from typing_extensions import Annotated

class InputEnum(str, Enum):
    option1 = "option1"
    option2 = "option2"
    option3 = "option3"

class InputObject(BaseModel):
    prop1: str = Field(
        default=None,
        description='Argument name.',
    )
    prop2: Union[str, list, int, float, bool, dict, date, datetime, time] = Field(
        default=None,
        description='Argument value.',
        json_schema_extra={
            "from_upstream": "always"
        }
    )

class InputModel(BaseModel):
    input_string: str = Field(
        default="default value",
        description='Input string to be logged.'
    )
    input_textarea: Optional[str] = Field(
        default=None,
        description='Input string to be logged.',
        json_schema_extra={
            'widget':"textarea",
        }
    )
    input_code: str = Field(
        default="print('Hello world!')",
        description='Input code to be logged.',
        json_schema_extra={
            'widget': "codeeditor",
        }
    )
    input_date: date = Field(
        default="2023-01-01",
        description='Input date to be logged.'
    )
    input_time: time = Field(
        default="16:20:00",
        description='Input time to be logged.',
    )
    input_datetime: datetime = Field(
        default="2023-01-01T16:20:00",
        description='Input datetime to be logged.'
    )
    input_integer: int = Field(
        default=10,
        description='Input integer to be logged.'
    )
    input_float: float = Field(
        default=10.5,
        description='Input float to be logged.'
    )
    input_float2: float = Field(
        default=0.1,
        description="Float with min and max",
        gt=0.,
        lt=1.
    ) 
    input_boolean: bool = Field(
        default=False,
        description='Input boolean to be logged.'
    )
    input_enum: InputEnum = Field(
        default=InputEnum.option1,
        description='Input enum to be logged.'
    )
    input_string_optional: Optional[str] = Field(
        default=None,
        description='Input enum to be logged.'
    )
    input_array_string: List[str] = Field(
        default=["default_1", "default_2", "default_3"],
        description='Input array to be logged.'
    )
    input_array_float: List[float] = Field(
        default=[10.1, 10.2, 10.3],
        description='Input array to be logged.'
    )
    input_array_float_2: List[Annotated[float, Gt(0.)]] = Field(
        default=[10.1, 10.2, 10.3],
        description='Input array to be logged.',
    )
    input_array_integer: List[int] = Field(
        default=[10 , 10 , 10 ],
        description='Input array to be logged.'
    )
    input_array_object: List[InputObject] = Field(
        default=[
            InputObject(prop1="",prop2=1)
        ]
    )

class OutputModel(BaseModel):
    message: str = Field(
        description="Output message to log"
    )
