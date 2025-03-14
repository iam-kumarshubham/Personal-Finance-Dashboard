from sqlalchemy.orm import Session
from app.repositories.liability_repository import LiabilityRepository
from app.schemas.liability import LiabilityCreate

class LiabilityService:
    @staticmethod
    def add_user_liability(db: Session, liability_data: LiabilityCreate, user_id: int):
        return LiabilityRepository.add_liability(db, liability_data, user_id)

    @staticmethod
    def get_user_liabilities(db: Session, user_id: int):
        return LiabilityRepository.get_liabilities_by_user(db, user_id)
