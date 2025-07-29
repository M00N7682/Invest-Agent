from typing import Dict, Any
from langchain_core.runnables import Runnable
import os
import httpx
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

class BackTesterAgent(Runnable):
    def invoke(self, state: Dict[str, Any]) -> Dict[str, Any]:
        import pandas as pd

        df = pd.DataFrame(state["market_data"])
        rule = state["parsed_strategy"]  # 예: "RSI < 30 and volume > MA20"

        # 조건 파싱 - 단순 텍스트 파싱 기반
        buy_condition = (df["RSI"] < 30) & (df["volume"] > df["MA20"])

        trades = []
        position = None
        entry_price = 0

        for i in range(len(df)):
            row = df.iloc[i]

            if not position and buy_condition.iloc[i]:
                position = "long"
                entry_price = row["close"]
                trades.append({"date": row["date"].strftime("%Y-%m-%d"), "type": "buy", "price": entry_price})

            elif position == "long" and row["RSI"] > 50:
                exit_price = row["close"]
                return_pct = (exit_price - entry_price) / entry_price
                trades.append({"date": row["date"].strftime("%Y-%m-%d"), "type": "sell", "price": exit_price, "return_pct": round(return_pct, 4)})
                position = None

        # 성과 지표 계산
        total_return = sum([t.get("return_pct", 0) for t in trades if t["type"] == "sell"])
        num_trades = len([t for t in trades if t["type"] == "sell"])
        avg_return = total_return / num_trades if num_trades > 0 else 0

        result = {
            "ROI": round(total_return, 4),
            "AvgReturn": round(avg_return, 4),
            "NumTrades": num_trades
        }

        return {**state, "backtest_result": result, "trade_logs": trades}
