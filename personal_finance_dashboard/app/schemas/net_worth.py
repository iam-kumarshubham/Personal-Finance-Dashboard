from pydantic import BaseModel

class NetWorthResponse(BaseModel):
    total_assets: float
    total_liabilities: float
    net_worth: float
