from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserCreate(UserLogin):
    name: str

class UserResponse(UserLogin):
    id: int
    email: EmailStr
    name: str
    created_at: datetime

    class Config:
        from_attributes = True
