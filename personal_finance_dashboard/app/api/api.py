from fastapi import APIRouter
from app.api.endpoints import auth, users, transactions, assets, liabilities, charts
from app.core.config import settings

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
api_router.include_router(assets.router, prefix="/assets", tags=["assets"])
api_router.include_router(liabilities.router, prefix="/liabilities", tags=["liabilities"])
api_router.include_router(charts.router, prefix="/charts", tags=["charts"]) 