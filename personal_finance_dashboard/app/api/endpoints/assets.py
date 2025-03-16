from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.asset import AssetCreate
from app.services.asset_service import AssetService
from app.db.session import get_db
from app.utils.dependencies import get_current_user

router = APIRouter()

@router.post("/")
def add_asset(asset_data: AssetCreate, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return AssetService.add_user_asset(db, asset_data, user_id)

@router.get("/")
def get_assets(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return AssetService.get_user_assets(db, user_id)
