from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, time, date


class InputModel(BaseModel):
    input_date: date = Field(
        description='input_date required.'
    )
    input_datetime: Optional[datetime] = Field(
        default=None,
        description='input_datetime with default=None.'
    )
    input_time: Optional[time] = Field(
        default="16:20:00",
        description='input_time not required time.',
    )

class OutputModel(BaseModel):
    input_date: date = Field(
        description='input_date required.'
    )
    input_datetime: Optional[datetime] = Field(
        default=None,
        description='input_datetime with default=None.'
    )
    input_time: Optional[time] = Field(
        default="16:20:00",
        description='input_time not required time.',
    )

