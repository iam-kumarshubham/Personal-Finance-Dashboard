from fastapi import FastAPI
from app.api.endpoints import auth, transactions, assets, liabilities, net_worth

app = FastAPI(title="Personal Finance API")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
app.include_router(assets.router, prefix="/assets", tags=["Assets"])
app.include_router(liabilities.router, prefix="/liabilities", tags=["Liabilities"])
app.include_router(net_worth.router, prefix="/net-worth", tags=["Net Worth"])
