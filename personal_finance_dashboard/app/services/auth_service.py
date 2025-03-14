from sqlalchemy.orm import Session
from app.repositories.asset_repository import AssetRepository
from app.schemas.asset import AssetCreate

class AssetService:
    @staticmethod
    def add_user_asset(db: Session, asset_data: AssetCreate, user_id: int):
        return AssetRepository.add_asset(db, asset_data, user_id)

    @staticmethod
    def get_user_assets(db: Session, user_id: int):
        return AssetRepository.get_assets_by_user(db, user_id)
