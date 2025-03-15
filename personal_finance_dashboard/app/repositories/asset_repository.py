from sqlalchemy.orm import Session
from models.asset import Asset
from schemas.asset import AssetCreate

class AssetRepository:
    @staticmethod
    def add_asset(db: Session, asset_data: AssetCreate, user_id: int):
        db_asset = Asset(**asset_data.dict(), user_id=user_id)
        db.add(db_asset)
        db.commit()
        db.refresh(db_asset)
        return db_asset

    @staticmethod
    def get_assets_by_user(db: Session, user_id: int):
        return db.query(Asset).filter(Asset.user_id == user_id).all()
