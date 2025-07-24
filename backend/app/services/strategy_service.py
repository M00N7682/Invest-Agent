from sqlalchemy.orm import Session
from models.schemas import StrategyCreate, Strategy
from database.crud import create_strategy, get_strategy, list_strategies

def create_strategy_service(db: Session, strategy_data: StrategyCreate):
    return create_strategy(db, strategy_data)

def get_strategy_service(db: Session, strategy_id: int):
    return get_strategy(db, strategy_id)

def list_strategies_service(db: Session):
    return list_strategies(db)