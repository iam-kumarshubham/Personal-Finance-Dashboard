from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin
from services.auth_service import AuthService
from db.session import get_db

router = APIRouter()

@router.post("/signup")
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        user = AuthService.register_user(db, user_data)
        return {"message": "User registered successfully", "user_id": user.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    token = AuthService.authenticate_user(db, user_data.email, user_data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}
