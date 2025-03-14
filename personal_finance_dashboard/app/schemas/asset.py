from pydantic import BaseModel
from typing import Literal

class AssetBase(BaseModel):
    name: str
    type: Literal["bank", "investment", "property"]
    value: float

class AssetCreate(AssetBase):
    pass

class AssetResponse(AssetBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
