from fastapi import APIRouter

router = APIRouter(prefix="/trades", tags=["trades"])

@router.get("/{strategy_id}")
def get_trades(strategy_id: int):
    """
    전략 백테스트 결과의 매수/매도 거래 로그 반환
    """
    # TODO: 거래 로그 반환 로직 구현
    return [
        {"date": "2024-01-01", "price": 10000, "return": 0.05, "type": "buy"},
        {"date": "2024-01-10", "price": 10500, "return": 0.03, "type": "sell"}
    ]