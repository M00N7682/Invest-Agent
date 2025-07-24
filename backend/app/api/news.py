from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import SessionLocal
from models.schemas import NewsItem
from typing import List

router = APIRouter(prefix="/news", tags=["news"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{strategy_id}", response_model=List[NewsItem])
def get_news(strategy_id: int, db: Session = Depends(get_db)):
    """
    거래일 기준으로 뉴스/공시 요약 반환
    """
    # TODO: 실제 DB 연동 및 서비스 로직으로 대체
    if strategy_id != 1:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return [
        NewsItem(date="2024-01-01", news="시장 급등"),
        NewsItem(date="2024-01-10", news="신규 상장 공시")
    ]