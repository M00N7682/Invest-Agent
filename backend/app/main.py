from fastapi import FastAPI
from api.strategy import router as strategy_router
from api.trade import router as trade_router
from api.metrics import router as metrics_router
from api.news import router as news_router
from api.report import router as report_router

app = FastAPI()

app.include_router(strategy_router)
app.include_router(trade_router)
app.include_router(metrics_router)
app.include_router(news_router)
app.include_router(report_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}