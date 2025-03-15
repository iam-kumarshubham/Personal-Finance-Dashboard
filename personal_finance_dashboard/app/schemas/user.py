from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserLogin(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserLogin):
    password: str

class UserResponse(UserLogin):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
