from sqlalchemy.orm import Session
from app.models.asset import Asset
from app.models.liability import Liability

class NetWorthRepository:
    @staticmethod
    def calculate_net_worth(db: Session, user_id: int):
        total_assets = db.query(Asset).filter(Asset.user_id == user_id).with_entities(Asset.value).all()
        total_liabilities = db.query(Liability).filter(Liability.user_id == user_id).with_entities(Liability.value).all()

        total_assets = sum(asset.value for asset in total_assets) if total_assets else 0
        total_liabilities = sum(liability.value for liability in total_liabilities) if total_liabilities else 0

        return {
            "total_assets": total_assets,
            "total_liabilities": total_liabilities,
            "net_worth": total_assets - total_liabilities
        }
