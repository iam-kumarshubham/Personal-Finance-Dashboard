from sqlalchemy.orm import Session
from repositories.transaction_repository import TransactionRepository
from schemas.transaction import TransactionCreate

class TransactionService:
    @staticmethod
    def add_transaction(db: Session, transaction_data: TransactionCreate, user_id: int):
        return TransactionRepository.create_transaction(db, transaction_data, user_id)

    @staticmethod
    def get_user_transactions(db: Session, user_id: int):
        return TransactionRepository.get_transactions_by_user(db, user_id)

    @staticmethod
    def remove_transaction(db: Session, transaction_id: int, user_id: int):
        return TransactionRepository.delete_transaction(db, transaction_id, user_id)
