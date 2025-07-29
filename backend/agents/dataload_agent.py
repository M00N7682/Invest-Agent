from typing import Dict, Any
from langchain_core.runnables import Runnable
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

class DataLoaderAgent(Runnable):
    def invoke(self, state: Dict[str, Any]) -> Dict[str, Any]:
        ticker = state["ticker"]
        start_date = state["start_date"]
        end_date = state["end_date"]

        # CSV 불러오기
        df = pd.read_csv(f"data/{ticker}.csv", parse_dates=["date"])
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)].copy()

        # 기술 지표 계산
        df["RSI"] = RSIIndicator(df["close"]).rsi()
        df["MA20"] = SMAIndicator(df["volume"], window=20).sma_indicator()

        # 필요한 컬럼만 정리
        df = df[["date", "open", "high", "low", "close", "volume", "RSI", "MA20"]]
        df = df.dropna().reset_index(drop=True)

        state["market_data"] = df.to_dict(orient="records")
        return state
