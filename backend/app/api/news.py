from fastapi import APIRouter

router = APIRouter(prefix="/news", tags=["news"])

@router.get("/{strategy_id}")
def get_news(strategy_id: int):
    """
    거래일 기준으로 뉴스/공시 요약 반환
    """
    # TODO: 뉴스/공시 반환 로직 구현
    return [
        {"date": "2024-01-01", "news": "시장 급등"},
        {"date": "2024-01-10", "news": "신규 상장 공시"}
    ]