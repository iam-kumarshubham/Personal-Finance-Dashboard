from sqlalchemy.orm import Session
from repositories.net_worth_repository import NetWorthRepository

class NetWorthService:
    @staticmethod
    def get_user_net_worth(db: Session, user_id: int):
        return NetWorthRepository.calculate_net_worth(db, user_id)
