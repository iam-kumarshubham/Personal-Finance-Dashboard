from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.hash import hash_password

class UserRepository:
    @staticmethod
    def create_user(db: Session, user_data: UserCreate):
        hashed_password = hash_password(user_data.password)
        db_user = User(email=user_data.email, name=user_data.name, password_hash=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()
