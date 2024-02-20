from pydantic import BaseModel, Field
from typing import Optional

class InputModel(BaseModel):
    input_float: float = Field(
        description='Input float required.'
    )
    input_float_optional: Optional[float] = Field(
        default=None,
        description='Input float with default=None.'
    )

class OutputModel(BaseModel):
    input_float: float = Field(
        description='input_float required float.'
    )
    input_float_optional: Optional[float] = Field(
        default=None,
        description='Input enum with default=None.'
    )
