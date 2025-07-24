from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import SessionLocal
from models.schemas import StrategyCreate, Strategy
from models.tables import StrategyTable
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
    strategy = create_strategy_service(db, strategy_data)
    return Strategy(
        id=strategy.id,
        name=strategy.name,
        description=strategy.description,
        conditions=strategy.conditions,
        status=strategy.status
    )

@router.get("/{strategy_id}", response_model=Strategy)
def get_strategy(strategy_id: int, db: Session = Depends(get_db)):
    strategy = get_strategy_service(db, strategy_id)
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return Strategy(
        id=strategy.id,
        name=strategy.name,
        description=strategy.description,
        conditions=strategy.conditions,
        status=strategy.status
    )

@router.get("/", response_model=list[Strategy])
def list_strategies(db: Session = Depends(get_db)):
    strategies = list_strategies_service(db)
    return [
        Strategy(
            id=s.id,
            name=s.name,
            description=s.description,
            conditions=s.conditions,
            status=s.status
        ) for s in strategies
    ]