from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from app.models.asset import AssetType

class AssetBase(BaseModel):
    name: str
    type: AssetType
    value: float
    description: Optional[str] = None

class AssetCreate(AssetBase):
    pass

class AssetUpdate(AssetBase):
    pass

class AssetInDBBase(AssetBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class Asset(AssetInDBBase):
    pass

class AssetInDB(AssetInDBBase):
    pass
