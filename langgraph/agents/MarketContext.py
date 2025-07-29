class MarketContextAgent(Runnable):
    def invoke(self, state: Dict[str, Any]) -> Dict[str, Any]:
        from datetime import datetime

        TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
        headers = {
            "Authorization": f"Bearer {TAVILY_API_KEY}"
        }

        trade_logs = state.get("trade_logs", [])
        ticker = state["ticker"]

        results = []
        for trade in trade_logs:
            date_str = trade["date"]
            query = f"{ticker} {date_str} 뉴스"
            response = httpx.post(
                "https://api.tavily.com/search",
                headers=headers,
                json={"query": query, "max_results": 3}
            )
            if response.status_code == 200:
                docs = response.json().get("results", [])
                summary = "\n".join([d.get("content", "")[:300] for d in docs])
                results.append({"date": date_str, "summary": summary})
            else:
                results.append({"date": date_str, "summary": "뉴스 수집 실패"})

        return {**state, "market_context": results}