from typing import List

from pydantic import BaseModel


class Countries(BaseModel):
    countries: List["Country"]


class Country(BaseModel):
    name: str
    pattern: str
    number_pattern: str
    number_example: str
    price: float
