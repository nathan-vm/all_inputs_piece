from pydantic import BaseModel, Field

class InputModel(BaseModel):
    input_boolean: bool = Field(
        default=False,
        description='input_boolean required boolean.'
    )

class OutputModel(BaseModel):
    input_boolean: bool = Field(
        description='input_boolean required boolean.'
    )
