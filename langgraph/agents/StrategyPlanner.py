class StrategyPlannerAgent(Runnable):
    def invoke(self, state: Dict[str, Any]) -> Dict[str, Any]:
        HYPERCLOVA_API_KEY = os.getenv("HYPERCLOVA_API_KEY")
        HYPERCLOVA_API_URL = os.getenv("HYPERCLOVA_API_URL")

        prompt = state["strategy_text"]
        headers = {
            "X-NCP-APIGW-API-KEY": HYPERCLOVA_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "text": f"'{prompt}' 전략을 기술 지표 조건으로 바꿔줘. 예시: RSI < 30 and Volume > MA20",
            "maxTokens": 256,
            "temperature": 0.4
        }

        response = httpx.post(HYPERCLOVA_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            parsed = response.json().get("result", "RSI < 30 and volume > MA20")
        else:
            parsed = "RSI < 30 and volume > MA20"

        return {**state, "parsed_strategy": parsed}