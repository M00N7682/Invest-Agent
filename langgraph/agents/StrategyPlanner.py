# StrategyPlannerAgent: 자연어 전략 입력 → 구조화된 룰 추출 (HyperCLOVA 활용)

class StrategyPlannerAgent:
    def __init__(self, llm_client=None):
        self.llm_client = llm_client  # HyperCLOVA API 클라이언트 등

    def plan(self, user_text: str) -> dict:
        """
        자연어 전략 설명을 받아 구조화된 룰(예: {'RSI': '<30', 'Vol': '>MA20'})로 변환
        """
        # 실제 구현에서는 HyperCLOVA 호출
        if self.llm_client:
            return self.llm_client.extract_rules(user_text)
        # 예시: 하드코딩
        return {"rule": "RSI<30 and Vol>MA20"}