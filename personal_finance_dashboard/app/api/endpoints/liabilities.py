from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.liability import LiabilityCreate
from app.services.liability_service import LiabilityService
from app.db.session import get_db
from app.utils.security import get_current_user

router = APIRouter()

@router.post("/")
def add_liability(liability_data: LiabilityCreate, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return LiabilityService.add_user_liability(db, liability_data, user_id)

@router.get("/")
def get_liabilities(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return LiabilityService.get_user_liabilities(db, user_id)
