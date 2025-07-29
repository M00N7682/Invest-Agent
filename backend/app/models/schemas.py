from pydantic import BaseModel
from typing import Optional, List

class StrategyCreate(BaseModel):
    name: str
    description: str
    conditions: str

class Strategy(BaseModel):
    id: int
    name: str
    description: str
    conditions: dict
    status: str

class Trade(BaseModel):
    date: str
    price: float
    return_rate: Optional[float] = None
    type: str  # "buy" or "sell"

class Metrics(BaseModel):
    CAGR: float
    MDD: float
    Sharpe: float

class NewsItem(BaseModel):
    date: str
    news: str

class Report(BaseModel):
    summary: str
    insight: str
    suggestion: str