from pydantic import BaseModel, Field
from typing import Optional

class InputModel(BaseModel):
    input_integer: int = Field(
        description="Input integer required.",
        from_upstream="allowed"
    )
    input_integer_optional: Optional[int] = Field(
        default=None,
        description="Input integer optional.",
        from_upstream="allowed"
    )

class OutputModel(BaseModel):
    input_integer: int = Field(
        description='input_integer required integer.',
    )
    input_integer_optional: Optional[int] = Field(
        description="Input integer optional.",
        default=None,
    )
