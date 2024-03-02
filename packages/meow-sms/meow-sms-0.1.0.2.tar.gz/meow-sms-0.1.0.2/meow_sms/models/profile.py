from pydantic import BaseModel, Field


class Profile(BaseModel):
    status: bool
    percent_rate: float | bool
    balance: float
    sent_sms: int = Field(..., alias="sent")
    sent_today: int
