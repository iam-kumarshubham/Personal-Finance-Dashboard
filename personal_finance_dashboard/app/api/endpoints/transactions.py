from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.transaction import TransactionCreate
from services.transaction_service import TransactionService
from db.session import get_db
from utils.dependencies import get_current_user

router = APIRouter()

@router.post("/")
def add_transaction(transaction_data: TransactionCreate, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return TransactionService.add_transaction(db, transaction_data, user_id)

@router.get("/")
def get_transactions(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return TransactionService.get_user_transactions(db, user_id)

@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    transaction = TransactionService.remove_transaction(db, transaction_id, user_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Transaction deleted successfully"}
