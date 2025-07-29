from fastapi import APIRouter
from agents.BackTesterAgent import BackTesterAgent

router = APIRouter(prefix="/backtester", tags=["Backtester"])
agent = BackTesterAgent()

@router.post("/")
def run_backtester(market_data: list[dict], parsed_strategy: str):
    state = {"market_data": market_data, "parsed_strategy": parsed_strategy}
    result = agent.invoke(state)
    return {
        "backtest_result": result["backtest_result"],
        "trade_logs": result["trade_logs"]
    }
                     