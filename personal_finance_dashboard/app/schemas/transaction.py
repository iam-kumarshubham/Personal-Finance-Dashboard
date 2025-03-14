from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class TransactionBase(BaseModel):
    type: Literal["income", "expense"]
    category: str
    amount: float
    date: datetime
    description: str | None = None

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
