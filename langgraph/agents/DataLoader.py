# DataLoaderAgent: 종목, 기간, 가격, 지표 데이터 확보 및 계산

class DataLoaderAgent:
    def __init__(self, data_source=None):
        self.data_source = data_source  # DB, API 등

    def load(self, symbol: str, start: str, end: str) -> dict:
        """
        종목, 기간에 맞는 가격/지표 데이터 로딩 및 전처리
        """
        # 실제 구현에서는 DB/API에서 데이터 조회
        # 예시: 하드코딩
        return {
            "prices": [100, 102, 105],
            "dates": ["2024-01-01", "2024-01-02", "2024-01-03"],
            "RSI": [28, 32, 35],
            "Vol": [1000, 1200, 1100],
            "MA20": [101, 102, 103]
        }