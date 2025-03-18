from datetime import datetime, timedelta
from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.models.transaction import Transaction
from app.models.asset import Asset
from app.models.liability import Liability
from app.api.deps import get_current_user
from app.schemas.chart import (
    NetWorthData,
    IncomeExpenseData,
    ChartSummary,
)

router = APIRouter()

@router.get("/net-worth", response_model=List[NetWorthData])
def get_net_worth_trend(
    start_date: str = Query(..., description="Start date in YYYY-MM-DD format"),
    end_date: str = Query(..., description="End date in YYYY-MM-DD format"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Get daily snapshots of assets and liabilities
    daily_data = []
    current_date = start
    
    while current_date <= end:
        # Get assets and liabilities for the current date
        assets = db.query(Asset).filter(
            Asset.user_id == current_user.id,
            Asset.created_at <= current_date
        ).all()
        
        liabilities = db.query(Liability).filter(
            Liability.user_id == current_user.id,
            Liability.created_at <= current_date
        ).all()
        
        total_assets = sum(asset.value for asset in assets)
        total_liabilities = sum(liability.amount for liability in liabilities)
        
        daily_data.append(NetWorthData(
            date=current_date.strftime("%Y-%m-%d"),
            assets=total_assets,
            liabilities=total_liabilities,
            netWorth=total_assets - total_liabilities
        ))
        
        current_date += timedelta(days=1)
    
    return daily_data

@router.get("/income-expense", response_model=List[IncomeExpenseData])
def get_income_expense(
    start_date: str = Query(..., description="Start date in YYYY-MM-DD format"),
    end_date: str = Query(..., description="End date in YYYY-MM-DD format"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Get daily income and expenses
    daily_data = []
    current_date = start
    
    while current_date <= end:
        # Get transactions for the current date
        transactions = db.query(Transaction).filter(
            Transaction.user_id == current_user.id,
            Transaction.date == current_date
        ).all()
        
        income = sum(t.amount for t in transactions if t.type == "income")
        expenses = sum(t.amount for t in transactions if t.type == "expense")
        
        daily_data.append(IncomeExpenseData(
            date=current_date.strftime("%Y-%m-%d"),
            income=income,
            expenses=expenses
        ))
        
        current_date += timedelta(days=1)
    
    return daily_data

@router.get("/summary", response_model=ChartSummary)
def get_chart_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Get current month's start and end dates
    today = datetime.now()
    month_start = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_month_start = (month_start - timedelta(days=1)).replace(day=1)
    
    # Get current assets and liabilities
    current_assets = db.query(Asset).filter(
        Asset.user_id == current_user.id,
        Asset.created_at <= today
    ).all()
    current_liabilities = db.query(Liability).filter(
        Liability.user_id == current_user.id,
        Liability.created_at <= today
    ).all()
    
    # Get last month's assets and liabilities
    last_month_assets = db.query(Asset).filter(
        Asset.user_id == current_user.id,
        Asset.created_at <= last_month_start
    ).all()
    last_month_liabilities = db.query(Liability).filter(
        Liability.user_id == current_user.id,
        Liability.created_at <= last_month_start
    ).all()
    
    # Calculate totals
    total_assets = sum(asset.value for asset in current_assets)
    total_liabilities = sum(liability.amount for liability in current_liabilities)
    net_worth = total_assets - total_liabilities
    
    last_month_total_assets = sum(asset.value for asset in last_month_assets)
    last_month_total_liabilities = sum(liability.amount for liability in last_month_liabilities)
    last_month_net_worth = last_month_total_assets - last_month_total_liabilities
    
    # Calculate changes
    asset_change = ((total_assets - last_month_total_assets) / last_month_total_assets * 100) if last_month_total_assets > 0 else 0
    liability_change = ((total_liabilities - last_month_total_liabilities) / last_month_total_liabilities * 100) if last_month_total_liabilities > 0 else 0
    net_worth_change = ((net_worth - last_month_net_worth) / last_month_net_worth * 100) if last_month_net_worth > 0 else 0
    
    # Get current month's income and expenses
    current_month_transactions = db.query(Transaction).filter(
        Transaction.user_id == current_user.id,
        Transaction.date >= month_start,
        Transaction.date <= today
    ).all()
    
    last_month_transactions = db.query(Transaction).filter(
        Transaction.user_id == current_user.id,
        Transaction.date >= last_month_start,
        Transaction.date < month_start
    ).all()
    
    monthly_income = sum(t.amount for t in current_month_transactions if t.type == "income")
    monthly_expenses = sum(t.amount for t in current_month_transactions if t.type == "expense")
    
    last_month_income = sum(t.amount for t in last_month_transactions if t.type == "income")
    income_change = ((monthly_income - last_month_income) / last_month_income * 100) if last_month_income > 0 else 0
    
    return ChartSummary(
        totalAssets=total_assets,
        totalLiabilities=total_liabilities,
        netWorth=net_worth,
        monthlyIncome=monthly_income,
        monthlyExpenses=monthly_expenses,
        assetChange=asset_change,
        liabilityChange=liability_change,
        netWorthChange=net_worth_change,
        incomeChange=income_change
    ) 