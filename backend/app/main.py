# main_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent_graph import agent_executor
import uvicorn

# 입력 모델 정의
class StrategyRequest(BaseModel):
    ticker: str
    start_date: str
    end_date: str
    strategy_text: str

# FastAPI 앱
app = FastAPI()

# API 엔드포인트
@app.post("/run_strategy/")
async def run_strategy(req: StrategyRequest):
    try:
        # LangGraph DAG 실행
        result = await agent_executor.ainvoke({
            "ticker": req.ticker,
            "start_date": req.start_date,
            "end_date": req.end_date,
            "strategy_text": req.strategy_text,
        })
        return {
            "report_summary": result.get("report_summary"),
            "autocode": result.get("autocode"),
            "backtest_result": result.get("backtest_result")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 개발용 실행
if __name__ == "__main__":
    uvicorn.run("main_api:app", host="0.0.0.0", port=8000, reload=True)
