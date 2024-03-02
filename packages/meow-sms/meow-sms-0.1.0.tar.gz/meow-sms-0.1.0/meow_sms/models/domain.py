from pydantic import BaseModel, Field, validator, field_validator


class DomainInfo(BaseModel):
    isBanned: bool = Field(..., alias="rt_check")
    isWorking: bool = Field(..., alias="a_check")

    @field_validator('isBanned')
    def invert_isBanned(cls, v):
        return not v
