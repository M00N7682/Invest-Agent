from langgraph.graph import StateGraph
from agents.StrategyPlanner import StrategyPlannerAgent
from agents.DataLoader import DataLoaderAgent
from agents.BackTester import BacktestExecutorAgent
from agents.MarketContext import MarketContextAgent
from agents.InsightReporter import InsightReporterAgent

# 1. Define state schema (state = Dict[str, Any])
state_schema = {
    "strategy_text": str,
    "ticker": str,
    "start_date": str,
    "end_date": str,
    "parsed_strategy": str,
    "dataframe": object,
    "trade_logs": list,
    "metrics": dict,
    "news_contexts": list,
    "report_summary": str,
    "recommendations": str
}

# 2. Create LangGraph DAG
builder = StateGraph(state_schema)

# 3. Add nodes
builder.add_node("planner", StrategyPlannerAgent())
builder.add_node("loader", DataLoaderAgent())
builder.add_node("executor", BacktestExecutorAgent())
builder.add_node("context", MarketContextAgent())
builder.add_node("reporter", InsightReporterAgent())

# 4. Connect edges
builder.set_entry_point("planner")
builder.add_edge("planner", "loader")
builder.add_edge("loader", "executor")

# 5. 병렬 처리: 백테스트 후 news context도 분석
builder.add_edge("executor", "context")
builder.add_edge("context", "reporter")

# 6. 종료 노드 지정
builder.set_finish_point("reporter")

# 7. Build
graph = builder.compile()
