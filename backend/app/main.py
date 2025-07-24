from fastapi import FastAPI
from api.strategy import router as strategy_router

app = FastAPI()

app.include_router(strategy_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}