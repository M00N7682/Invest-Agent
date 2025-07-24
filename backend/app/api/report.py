from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import SessionLocal
from models.schemas import Report

router = APIRouter(prefix="/report", tags=["report"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{strategy_id}", response_model=Report)
def get_report(strategy_id: int, db: Session = Depends(get_db)):
    # TODO: 실제 DB 연동 및 서비스 로직으로 대체
    if strategy_id != 1:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return Report(
        summary="전략 요약 예시",
        insight="시장 상황에 따라 변동성이 큼",
        suggestion="리스크 관리 강화 필요"
    )