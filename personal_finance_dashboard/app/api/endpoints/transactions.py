from typing import Any, List, Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Transaction])
def read_transactions(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve transactions.
    """
    transactions = crud.transaction.get_by_user(
        db=db, user_id=current_user.id, skip=skip, limit=limit
    )
    return transactions

@router.post("/", response_model=schemas.Transaction)
def create_transaction(
    *,
    db: Session = Depends(deps.get_db),
    transaction_in: schemas.TransactionCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new transaction.
    """
    transaction_data = transaction_in.dict()
    transaction_data["user_id"] = current_user.id
    transaction = crud.transaction.create(db=db, obj_in=schemas.TransactionCreate(**transaction_data))
    return transaction

@router.put("/{transaction_id}", response_model=schemas.Transaction)
def update_transaction(
    *,
    db: Session = Depends(deps.get_db),
    transaction_id: int,
    transaction_in: schemas.TransactionUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a transaction.
    """
    transaction = crud.transaction.get(db=db, id=transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    if transaction.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    transaction = crud.transaction.update(
        db=db, db_obj=transaction, obj_in=transaction_in
    )
    return transaction

@router.get("/{transaction_id}", response_model=schemas.Transaction)
def read_transaction(
    *,
    db: Session = Depends(deps.get_db),
    transaction_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get transaction by ID.
    """
    transaction = crud.transaction.get(db=db, id=transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    if transaction.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return transaction

@router.delete("/{transaction_id}", response_model=schemas.Transaction)
def delete_transaction(
    *,
    db: Session = Depends(deps.get_db),
    transaction_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a transaction.
    """
    transaction = crud.transaction.get(db=db, id=transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    if transaction.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    transaction = crud.transaction.remove(db=db, id=transaction_id)
    return transaction

@router.get("/summary/", response_model=dict)
def get_transaction_summary(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
) -> Any:
    """
    Get transaction summary for a date range.
    """
    return crud.transaction.get_summary(
        db=db, user_id=current_user.id, start_date=start_date, end_date=end_date
    )
