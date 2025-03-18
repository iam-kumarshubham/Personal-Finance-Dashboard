from pydantic import BaseModel
from typing import List

class NetWorthData(BaseModel):
    date: str
    assets: float
    liabilities: float
    netWorth: float

class IncomeExpenseData(BaseModel):
    date: str
    income: float
    expenses: float

class ChartSummary(BaseModel):
    totalAssets: float
    totalLiabilities: float
    netWorth: float
    monthlyIncome: float
    monthlyExpenses: float
    assetChange: float
    liabilityChange: float
    netWorthChange: float
    incomeChange: float 