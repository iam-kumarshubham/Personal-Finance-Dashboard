from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate

class TransactionRepository:
    @staticmethod
    def create_transaction(db: Session, transaction_data: TransactionCreate, user_id: int):
        db_transaction = Transaction(**transaction_data.dict(), user_id=user_id)
        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)
        return db_transaction

    @staticmethod
    def get_transactions_by_user(db: Session, user_id: int):
        return db.query(Transaction).filter(Transaction.user_id == user_id).all()

    @staticmethod
    def delete_transaction(db: Session, transaction_id: int, user_id: int):
        transaction = db.query(Transaction).filter(Transaction.id == transaction_id, Transaction.user_id == user_id).first()
        if transaction:
            db.delete(transaction)
            db.commit()
        return transaction
