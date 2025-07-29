from fastapi import APIRouter
from agents.MarketContextAgent import MarketContextAgent

router = APIRouter(prefix="/market-context", tags=["Market Context"])
agent = MarketContextAgent()

@router.post("/")
def run_market_context(ticker: str, trade_logs: list[dict]):
    state = {"ticker": ticker, "trade_logs": trade_logs}
    result = agent.invoke(state)
    return result["market_context"]
