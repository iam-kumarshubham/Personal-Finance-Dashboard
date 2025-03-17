from pydantic import BaseModel

class NetWorth(BaseModel):
    total_assets: float
    total_liabilities: float
    net_worth: float

    class Config:
        from_attributes = True
