from pydantic import BaseModel, Field


class SendSms(BaseModel):
    text: str
    shortened_link: str = Field(..., alias="cuted_link")
    balance: float
    balance_after: float = Field(..., alias="sent_before")
    message_id: int


class SendCustomSms(BaseModel):
    price: float
    balance: float
    balance_after: float = Field(..., alias="sent_before")
    message_id: int


class SmsStatus(BaseModel):
    status: bool
