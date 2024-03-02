from typing import List

from pydantic import BaseModel, Field


class Services(BaseModel):
    services: List["Service"]


class Service(BaseModel):
    name: str
    pattern: str
    number_pattern: str
    number_example: str
    price: float
    sid: str
    version_1: str = Field(..., alias="text_1")
    version_2: str = Field(..., alias="text_2")
    refund: str = Field(..., alias="text_3")
