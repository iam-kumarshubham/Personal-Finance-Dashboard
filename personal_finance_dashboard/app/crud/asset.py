from typing import List
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate

class CRUDAsset(CRUDBase[Asset, AssetCreate, AssetUpdate]):
    def get_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Asset]:
        return (
            db.query(self.model)
            .filter(Asset.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_type(
        self,
        db: Session,
        *,
        user_id: int,
        type: str,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Asset]:
        return (
            db.query(self.model)
            .filter(Asset.user_id == user_id, Asset.type == type)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_total_value(self, db: Session, *, user_id: int) -> float:
        assets = self.get_by_user(db, user_id=user_id)
        return sum(asset.value for asset in assets)

asset = CRUDAsset(Asset) 