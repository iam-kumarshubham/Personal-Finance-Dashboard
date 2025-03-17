from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from app.models.transaction import TransactionType

class TransactionBase(BaseModel):
    type: TransactionType
    category: str
    amount: float
    description: Optional[str] = None
    date: datetime

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class TransactionInDBBase(TransactionBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class Transaction(TransactionInDBBase):
    pass

class TransactionInDB(TransactionInDBBase):
    pass
