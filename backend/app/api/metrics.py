from fastapi import APIRouter

router = APIRouter(prefix="/metrics", tags=["metrics"])

@router.get("/{strategy_id}")
def get_metrics(strategy_id: int):
    """
    전략의 성과 요약 지표(CAGR, MDD, Sharpe 등) 조회
    """
    # TODO: 성과 지표 반환 로직 구현
    return {
        "CAGR": 0.12,
        "MDD": -0.08,
        "Sharpe": 1.5
    }