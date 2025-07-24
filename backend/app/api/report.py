from fastapi import APIRouter

router = APIRouter(prefix="/report", tags=["report"])

@router.get("/{strategy_id}")
def get_report(strategy_id: int):
    """
    HyperCLOVA 기반 전략 통찰 및 개선 요약 반환
    """
    # TODO: 전략 요약, 인사이트, 제안 반환 로직 구현
    return {
        "summary": "전략 요약 예시",
        "insight": "시장 상황에 따라 변동성이 큼",
        "suggestion": "리스크 관리 강화 필요"
    }