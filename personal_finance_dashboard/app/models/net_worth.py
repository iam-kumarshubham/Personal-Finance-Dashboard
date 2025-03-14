from sqlalchemy.orm import Session
from app.models.asset import Asset
from app.models.liability import Liability

def calculate_net_worth(db: Session, user_id: int):
    total_assets = db.query(Asset).filter(Asset.user_id == user_id).sum(Asset.value) or 0
    total_liabilities = db.query(Liability).filter(Liability.user_id == user_id).sum(Liability.value) or 0
    return {
        "total_assets": total_assets,
        "total_liabilities": total_liabilities,
        "net_worth": total_assets - total_liabilities
    }
