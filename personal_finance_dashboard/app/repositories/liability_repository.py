from sqlalchemy.orm import Session
from models.liability import Liability
from schemas.liability import LiabilityCreate

class LiabilityRepository:
    @staticmethod
    def add_liability(db: Session, liability_data: LiabilityCreate, user_id: int):
        db_liability = Liability(**liability_data.dict(), user_id=user_id)
        db.add(db_liability)
        db.commit()
        db.refresh(db_liability)
        return db_liability

    @staticmethod
    def get_liabilities_by_user(db: Session, user_id: int):
        return db.query(Liability).filter(Liability.user_id == user_id).all()
