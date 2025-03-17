from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.crud.base import CRUDBase
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate

class CRUDTransaction(CRUDBase[Transaction, TransactionCreate, TransactionUpdate]):
    def get_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Transaction]:
        return (
            db.query(self.model)
            .filter(Transaction.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_date_range(
        self,
        db: Session,
        *,
        user_id: int,
        start_date: datetime,
        end_date: datetime,
    ) -> List[Transaction]:
        return (
            db.query(self.model)
            .filter(
                Transaction.user_id == user_id,
                Transaction.date >= start_date,
                Transaction.date <= end_date,
            )
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
    ) -> List[Transaction]:
        return (
            db.query(self.model)
            .filter(Transaction.user_id == user_id, Transaction.type == type)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_category(
        self,
        db: Session,
        *,
        user_id: int,
        category: str,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Transaction]:
        return (
            db.query(self.model)
            .filter(Transaction.user_id == user_id, Transaction.category == category)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_summary(
        self,
        db: Session,
        *,
        user_id: int,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> dict:
        if not start_date:
            start_date = datetime.now() - timedelta(days=30)
        if not end_date:
            end_date = datetime.now()

        transactions = self.get_by_date_range(
            db, user_id=user_id, start_date=start_date, end_date=end_date
        )

        total_income = sum(
            t.amount for t in transactions if t.type == "income"
        )
        total_expenses = sum(
            t.amount for t in transactions if t.type == "expense"
        )

        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_income": total_income - total_expenses,
            "period_start": start_date,
            "period_end": end_date,
        }

transaction = CRUDTransaction(Transaction) 