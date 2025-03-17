from typing import List
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.liability import Liability
from app.schemas.liability import LiabilityCreate, LiabilityUpdate

class CRUDLiability(CRUDBase[Liability, LiabilityCreate, LiabilityUpdate]):
    def get_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Liability]:
        return (
            db.query(self.model)
            .filter(Liability.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_type(
        self,
        db: Session,
        *,
        user_id: int,
        type: str,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Liability]:
        return (
            db.query(self.model)
            .filter(Liability.user_id == user_id, Liability.type == type)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_total_value(self, db: Session, *, user_id: int) -> float:
        liabilities = self.get_by_user(db, user_id=user_id)
        return sum(liability.value for liability in liabilities)

liability = CRUDLiability(Liability) 