from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Liability])
def read_liabilities(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve liabilities.
    """
    liabilities = crud.liability.get_by_user(
        db=db, user_id=current_user.id, skip=skip, limit=limit
    )
    return liabilities

@router.post("/", response_model=schemas.Liability)
def create_liability(
    *,
    db: Session = Depends(deps.get_db),
    liability_in: schemas.LiabilityCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new liability.
    """
    liability = crud.liability.create_with_user(
        db=db, obj_in=liability_in, user_id=current_user.id
    )
    return liability

@router.put("/{liability_id}", response_model=schemas.Liability)
def update_liability(
    *,
    db: Session = Depends(deps.get_db),
    liability_id: int,
    liability_in: schemas.LiabilityUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a liability.
    """
    liability = crud.liability.get(db=db, id=liability_id)
    if not liability:
        raise HTTPException(status_code=404, detail="Liability not found")
    if liability.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    liability = crud.liability.update(
        db=db, db_obj=liability, obj_in=liability_in
    )
    return liability

@router.get("/{liability_id}", response_model=schemas.Liability)
def read_liability(
    *,
    db: Session = Depends(deps.get_db),
    liability_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get liability by ID.
    """
    liability = crud.liability.get(db=db, id=liability_id)
    if not liability:
        raise HTTPException(status_code=404, detail="Liability not found")
    if liability.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return liability

@router.delete("/{liability_id}", response_model=schemas.Liability)
def delete_liability(
    *,
    db: Session = Depends(deps.get_db),
    liability_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a liability.
    """
    liability = crud.liability.get(db=db, id=liability_id)
    if not liability:
        raise HTTPException(status_code=404, detail="Liability not found")
    if liability.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    liability = crud.liability.remove(db=db, id=liability_id)
    return liability

@router.get("/total/", response_model=float)
def get_total_liabilities(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get total value of all liabilities.
    """
    return crud.liability.get_total_value(db=db, user_id=current_user.id)
