from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=dict)
def get_net_worth(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Calculate net worth (assets - liabilities).
    """
    total_assets = crud.asset.get_total_value(db=db, user_id=current_user.id)
    total_liabilities = crud.liability.get_total_value(db=db, user_id=current_user.id)
    
    return {
        "total_assets": total_assets,
        "total_liabilities": total_liabilities,
        "net_worth": total_assets - total_liabilities,
    }

