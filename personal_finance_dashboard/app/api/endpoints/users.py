from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserInDB
from app.api.deps import get_current_user
from app.core.security import get_password_hash

router = APIRouter()

@router.get("/me", response_model=UserInDB)
def read_users_me(
    current_user: User = Depends(get_current_user),
):
    """
    Get current user.
    """
    return current_user

@router.put("/me", response_model=UserInDB)
def update_user_me(
    *,
    db: Session = Depends(get_db),
    user_in: UserUpdate,
    current_user: User = Depends(get_current_user),
):
    """
    Update own user.
    """
    if user_in.password is not None:
        current_user.hashed_password = get_password_hash(user_in.password)
    if user_in.email is not None:
        current_user.email = user_in.email
    if user_in.full_name is not None:
        current_user.full_name = user_in.full_name
    if user_in.is_active is not None:
        current_user.is_active = user_in.is_active
    if user_in.is_superuser is not None:
        current_user.is_superuser = user_in.is_superuser
    
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user 