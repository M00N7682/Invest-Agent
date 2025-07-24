from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import SessionLocal
from models.schemas import Metrics
from models.tables import StrategyTable

router = APIRouter(prefix="/metrics", tags=["metrics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def calculate_metrics(strategy: StrategyTable) -> Metrics:
    # TODO: 실제 백테스트 결과 기반 계산 로직으로 대체
    if strategy.id == 1:
        return Metrics(CAGR=0.12, MDD=-0.08, Sharpe=1.5)
    else:
        return Metrics(CAGR=0.08, MDD=-0.12, Sharpe=1.1)

@router.get("/{strategy_id}", response_model=Metrics)
def get_metrics(strategy_id: int, db: Session = Depends(get_db)):
    strategy = db.query(StrategyTable).filter(StrategyTable.id == strategy_id).first()
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return calculate_metrics(strategy)