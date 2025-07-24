from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import SessionLocal
from models.schemas import StrategyCreate, Strategy
from services.strategy_service import (
    create_strategy_service,
    get_strategy_service,
    list_strategies_service,
)

router = APIRouter(prefix="/strategies", tags=["strategies"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Strategy)
def create_strategy(strategy_data: StrategyCreate, db: Session = Depends(get_db)):
    return create_strategy_service(db, strategy_data)

@router.get("/{strategy_id}", response_model=Strategy)
def get_strategy(strategy_id: int, db: Session = Depends(get_db)):
    strategy = get_strategy_service(db, strategy_id)
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return strategy

@router.get("/", response_model=list[Strategy])
def list_strategies(db: Session = Depends(get_db)):
    return list_strategies_service(db)