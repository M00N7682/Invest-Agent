from sqlalchemy.orm import Session
from models.tables import StrategyTable
from models.schemas import StrategyCreate

def create_strategy(db: Session, strategy: StrategyCreate):
    db_strategy = StrategyTable(
        name=strategy.name,
        description=strategy.description,
        conditions=strategy.conditions,
        status="created"
    )
    db.add(db_strategy)
    db.commit()
    db.refresh(db_strategy)
    return db_strategy

def get_strategy(db: Session, strategy_id: int):
    return db.query(StrategyTable).filter(StrategyTable.id == strategy_id).first()

def list_strategies(db: Session):
    return db.query(StrategyTable).all()