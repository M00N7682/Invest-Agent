from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import SessionLocal
from models.schemas import Trade
from typing import List

router = APIRouter(prefix="/trades", tags=["trades"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{strategy_id}", response_model=List[Trade])
def get_trades(strategy_id: int, db: Session = Depends(get_db)):
    """
    전략 백테스트 결과의 매수/매도 거래 로그 반환
    """
    # TODO: 실제 DB 연동 및 서비스 로직으로 대체
    if strategy_id != 1:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return [
        Trade(date="2024-01-01", price=10000, return_rate=0.05, type="buy"),
        Trade(date="2024-01-10", price=10500, return_rate=0.03, type="sell")
    ]