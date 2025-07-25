# MarketContextAgent: 거래일별 뉴스/공시 수집 및 요약 (HyperCLOVA 활용)
import requests

class MarketContextAgent:
    def __init__(self, tavily_api_key: str, llm_client=None):
        self.tavily_api_key = tavily_api_key
        self.llm_client = llm_client  # HyperCLOVA 등

    def get_context(self, dates: list, symbol: str) -> list:
        """
        거래일별 뉴스/공시 Tavily API로 수집 및 HyperCLOVA 요약
        """
        results = []
        for date in dates:
            # Tavily API 예시 요청 (실제 엔드포인트/파라미터는 Tavily 문서 참고)
            response = requests.get(
                "https://api.tavily.com/search",
                params={
                    "query": f"{symbol} 뉴스 OR 공시",
                    "date": date,
                    "api_key": self.tavily_api_key
                }
            )
            news_items = response.json().get("results", [])
            # 뉴스 요약 (HyperCLOVA 활용)
            if self.llm_client and news_items:
                summary = self.llm_client.summarize("\n".join([item["title"] for item in news_items]))
            else:
                summary = "; ".join([item["title"] for item in news_items])
            results.append({"date": date, "news": summary})
        return results