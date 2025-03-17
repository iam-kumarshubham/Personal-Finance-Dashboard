from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from app.models.liability import LiabilityType

class LiabilityBase(BaseModel):
    name: str
    type: LiabilityType
    value: float
    description: Optional[str] = None

class LiabilityCreate(LiabilityBase):
    pass

class LiabilityUpdate(LiabilityBase):
    pass

class LiabilityInDBBase(LiabilityBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class Liability(LiabilityInDBBase):
    pass

class LiabilityInDB(LiabilityInDBBase):
    pass
