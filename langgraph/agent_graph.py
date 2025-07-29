# agent_graph.py
from langgraph.graph import StateGraph, END
from langchain_core.runnables import Runnable

from BackTester import BackTesterAgent
from DataLoader import DataLoaderAgent
from InsightReporter import InsightReporterAgent
from MarketContext import MarketContextAgent
from StrategyPlanner import StrategyPlannerAgent

# 상태 타입 정의
from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict):
    ticker: str
    start_date: str
    end_date: str
    strategy_text: str
    parsed_strategy: str
    market_data: List[Dict[str, Any]]
    market_context: str
    backtest_result: Dict[str, Any]
    report_summary: str
    autocode: str

# Graph 생성
workflow = StateGraph(AgentState)

# 노드 등록
workflow.add_node("loader", DataLoaderAgent())
workflow.add_node("market", MarketContextAgent())
workflow.add_node("strategy", StrategyPlannerAgent())
workflow.add_node("backtest", BackTesterAgent())
workflow.add_node("insight", InsightReporterAgent())

# 엣지 구성
workflow.set_entry_point("loader")
workflow.add_edge("loader", "market")
workflow.add_edge("market", "strategy")
workflow.add_edge("strategy", "backtest")
workflow.add_edge("backtest", "insight")
workflow.add_edge("insight", END)

# Runnable로 export
agent_executor = workflow.compile()