from fastapi import APIRouter
from agents.InsightReporterAgent import InsightReporterAgent

router = APIRouter(prefix="/insight-reporter", tags=["Insight Reporter"])
agent = InsightReporterAgent()

@router.post("/")
def run_insight_reporter(backtest_result: dict, parsed_strategy: str, market_context: list[dict]):
    state = {
        "backtest_result": backtest_result,
        "parsed_strategy": parsed_strategy,
        "market_context": market_context
    }
    result = agent.invoke(state)
    return {
        "report_summary": result["report_summary"],
        "autocode": result["autocode"]
    }
