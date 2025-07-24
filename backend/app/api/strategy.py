from fastapi import APIRouter
from typing import Optional

router = APIRouter(prefix="/strategies", tags=["strategies"])

@router.post("/")
def create_strategy(strategy_data: dict):
    """
    사용자의 전략 아이디어와 조건을 입력받아 LangGraph 실행
    """
    # TODO: LangGraph 실행 및 전략 생성 로직 구현
    return {"strategy_id": 1, "message": "전략 생성 완료"}

@router.get("/{strategy_id}")
def get_strategy(strategy_id: int):
    """
    특정 전략의 상태 및 메타 정보 조회
    """
    # TODO: 전략 상태 및 메타 정보 반환 로직 구현
    return {
        "strategy_id": strategy_id,
        "strategy_text": "예시 전략",
        "period": "2020-2024",
        "status": "완료"
    }

@router.get("/")
def list_strategies(user_id: Optional[int] = None):
    """
    전체 전략 리스트 조회 (옵션: 사용자별)
    """
    # TODO: 전략 목록 반환 로직 구현
    return [
        {"strategy_id": 1, "summary": "전략 요약", "user_id": 1},
        {"strategy_id": 2, "summary": "다른 전략", "user_id": 2}
    ]