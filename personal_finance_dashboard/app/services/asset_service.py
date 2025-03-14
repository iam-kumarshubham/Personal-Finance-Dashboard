from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.utils.security import verify_password, create_jwt_token
from app.schemas.user import UserCreate

class AuthService:
    @staticmethod
    def register_user(db: Session, user_data: UserCreate):
        existing_user = UserRepository.get_user_by_email(db, user_data.email)
        if existing_user:
            raise ValueError("User already exists")
        return UserRepository.create_user(db, user_data)

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str):
        user = UserRepository.get_user_by_email(db, email)
        if not user or not verify_password(password, user.password_hash):
            return None
        return create_jwt_token({"sub": user.email})
