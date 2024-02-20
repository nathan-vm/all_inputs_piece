from pydantic import BaseModel, Field
from enum import Enum

class InputEnumStr(str, Enum):
    option1 = "option1"
    option2 = "option2"
    option3 = "option3"

class InputEnumInt(int, Enum):
    option1 = 1
    option2 = 2
    option3 = 3

class InputEnumFloat(float, Enum):
    option1 = 10.1
    option2 = 20.2
    option3 = 30.3

class InputModel(BaseModel):
    input_enum_string: InputEnumStr = Field(
        description='Input string required.'
    )
    input_enum_int: InputEnumInt = Field(
        description='Input integer required.'
    )
    input_enum_float: InputEnumFloat = Field(
        description='Input float required.'
    )


class OutputModel(BaseModel):
    input_enum_string: InputEnumStr = Field(
        description='Input string required.'
    )
    input_enum_int: InputEnumInt = Field(
        description='Input integer required.'
    )
    input_enum_float: InputEnumFloat = Field(
        description='Input float required.'
    )

