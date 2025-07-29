from fastapi import APIRouter
from agents.StrategyPlannerAgent import StrategyPlannerAgent

router = APIRouter(prefix="/strategy-planner", tags=["Strategy Planner"])
agent = StrategyPlannerAgent()

@router.post("/")
def run_strategy_planner(strategy_text: str):
    state = {"strategy_text": strategy_text}
    result = agent.invoke(state)
    return result["parsed_strategy"]
