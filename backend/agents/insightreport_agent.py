from typing import Dict, Any
from langchain_core.runnables import Runnable
import os
import httpx
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

class InsightReporterAgent(Runnable):
    def invoke(self, state: Dict[str, Any]) -> Dict[str, Any]:
        HYPERCLOVA_API_KEY = os.getenv("HYPERCLOVA_API_KEY")
        HYPERCLOVA_API_URL = os.getenv("HYPERCLOVA_API_URL")

        summary_prompt = f"""
        다음은 전략 성과입니다. 결과를 기반으로 한 전략 리포트입니다.

        전략 조건: {state.get("parsed_strategy")}
        ROI: {state['backtest_result']['ROI']}
        평균 수익률: {state['backtest_result']['AvgReturn']}
        거래 횟수: {state['backtest_result']['NumTrades']}
        뉴스 정보:
        {state.get('market_context', [])[:2]}
        """

        code_prompt = f"""
        다음 조건에 해당하는 백테스트용 파이썬 코드를 작성해줘:
        - 조건: {state.get('parsed_strategy')}
        - Pandas 기반으로 작성, CSV로부터 데이터 읽기
        - 진입 조건 충족 시 매수, RSI > 50일 때 매도
        - 수익률 계산 포함
        """

        headers = {
            "X-NCP-APIGW-API-KEY": HYPERCLOVA_API_KEY,
            "Content-Type": "application/json"
        }

        summary_payload = {"text": summary_prompt, "maxTokens": 512, "temperature": 0.4}
        code_payload = {"text": code_prompt, "maxTokens": 512, "temperature": 0.2}

        summary_resp = httpx.post(HYPERCLOVA_API_URL, headers=headers, json=summary_payload)
        code_resp = httpx.post(HYPERCLOVA_API_URL, headers=headers, json=code_payload)

        summary = summary_resp.json().get("result", "리포트 생성 실패")
        code = code_resp.json().get("result", "코드 생성 실패")

        return {
            **state,
            "report_summary": summary,
            "autocode": code
        }