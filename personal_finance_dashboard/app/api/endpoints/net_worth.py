from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.net_worth_service import NetWorthService
from db.session import get_db
from utils.dependencies import get_current_user

router = APIRouter()

@router.get("/")
def get_net_worth(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return NetWorthService.get_user_net_worth(db, user_id)
