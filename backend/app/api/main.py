from fastapi import FastAPI
from app.api import market_context, data_loader, strategy_planner, backtester, insight_reporter

app = FastAPI()

app.include_router(market_context.router)
app.include_router(data_loader.router)
app.include_router(strategy_planner.router)
app.include_router(backtester.router)
app.include_router(insight_reporter.router)
