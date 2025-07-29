from fastapi import FastAPI, Request
from agents.marketcontext_agent import MarketContextAgent
from agents.dataload_agent import DataLoaderAgent
from agents.strategyplanenr_agent import StrategyPlannerAgent
from agents.backtest_agent import BackTesterAgent
from agents.insightreport_agent import InsightReporterAgent

app = FastAPI()

# 각 에이전트 인스턴스화
market_context_agent = MarketContextAgent()
data_loader_agent = DataLoaderAgent()
strategy_planner_agent = StrategyPlannerAgent()
backtester_agent = BackTesterAgent()
insight_reporter_agent = InsightReporterAgent()

@app.post("/agents/market-context")
async def run_market_context(request: Request):
    state = await request.json()
    return market_context_agent.invoke(state)

@app.post("/agents/data-loader")
async def run_data_loader(request: Request):
    state = await request.json()
    return data_loader_agent.invoke(state)

@app.post("/agents/strategy-planner")
async def run_strategy_planner(request: Request):
    state = await request.json()
    return strategy_planner_agent.invoke(state)

@app.post("/agents/backtester")
async def run_backtester(request: Request):
    state = await request.json()
    return backtester_agent.invoke(state)

@app.post("/agents/insight-reporter")
async def run_insight_reporter(request: Request):
    state = await request.json()
    return insight_reporter_agent.invoke(state)
