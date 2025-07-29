from fastapi import APIRouter
from agents.DataLoaderAgent import DataLoaderAgent

router = APIRouter(prefix="/data-loader", tags=["Data Loader"])
agent = DataLoaderAgent()

@router.post("/")
def run_data_loader(ticker: str, start_date: str, end_date: str):
    state = {"ticker": ticker, "start_date": start_date, "end_date": end_date}
    result = agent.invoke(state)
    return result["market_data"]
