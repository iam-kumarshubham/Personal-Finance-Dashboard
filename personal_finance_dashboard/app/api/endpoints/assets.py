from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.asset import AssetCreate
from services.asset_service import AssetService
from db.session import get_db
from utils.dependencies import get_current_user

router = APIRouter()

@router.post("/")
def add_asset(asset_data: AssetCreate, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return AssetService.add_user_asset(db, asset_data, user_id)

@router.get("/")
def get_assets(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return AssetService.get_user_assets(db, user_id)
