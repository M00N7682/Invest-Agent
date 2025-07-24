# InsightReporterAgent: 전략의 해석, 리포트 자동 생성 (HyperCLOVA 활용)

class InsightReporterAgent:
    def __init__(self, llm_client=None):
        self.llm_client = llm_client  # HyperCLOVA 등

    def report(self, metrics: dict, context: list) -> dict:
        """
        성과 분석 + 시장 상황 기반 요약 보고서 생성
        """
        # 실제 구현에서는 HyperCLOVA 호출
        # 예시: 하드코딩
        return {
            "summary": "전략 요약 예시",
            "insight": "시장 상황에 따라 변동성이 큼",
            "suggestion": "리스크 관리 강화 필요"
        }