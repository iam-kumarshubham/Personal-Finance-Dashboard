from pydantic import BaseModel
from typing import Literal

class LiabilityBase(BaseModel):
    name: str
    type: Literal["loan", "credit card"]
    value: float

class LiabilityCreate(LiabilityBase):
    pass

class LiabilityResponse(LiabilityBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
