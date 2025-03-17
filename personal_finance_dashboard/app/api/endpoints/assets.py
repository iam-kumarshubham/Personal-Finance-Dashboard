from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Asset])
def read_assets(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve assets.
    """
    assets = crud.asset.get_by_user(
        db=db, user_id=current_user.id, skip=skip, limit=limit
    )
    return assets

@router.post("/", response_model=schemas.Asset)
def create_asset(
    *,
    db: Session = Depends(deps.get_db),
    asset_in: schemas.AssetCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new asset.
    """
    asset = crud.asset.create_with_user(
        db=db, obj_in=asset_in, user_id=current_user.id
    )
    return asset

@router.put("/{asset_id}", response_model=schemas.Asset)
def update_asset(
    *,
    db: Session = Depends(deps.get_db),
    asset_id: int,
    asset_in: schemas.AssetUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an asset.
    """
    asset = crud.asset.get(db=db, id=asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    if asset.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    asset = crud.asset.update(
        db=db, db_obj=asset, obj_in=asset_in
    )
    return asset

@router.get("/{asset_id}", response_model=schemas.Asset)
def read_asset(
    *,
    db: Session = Depends(deps.get_db),
    asset_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get asset by ID.
    """
    asset = crud.asset.get(db=db, id=asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    if asset.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return asset

@router.delete("/{asset_id}", response_model=schemas.Asset)
def delete_asset(
    *,
    db: Session = Depends(deps.get_db),
    asset_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an asset.
    """
    asset = crud.asset.get(db=db, id=asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    if asset.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    asset = crud.asset.remove(db=db, id=asset_id)
    return asset

@router.get("/total/", response_model=float)
def get_total_assets(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get total value of all assets.
    """
    return crud.asset.get_total_value(db=db, user_id=current_user.id)
