from utils.llm_client import LLMClient


class TrendAgent:

    @staticmethod
    def evaluate(signals, deviations):

        system_prompt = """
You are TrendAgent inside a cardiac cognitive AI swarm.

Role:
Interprets deviation dynamics, temporal drift, trajectory patterns.

CRITICAL RESPONSE RULES:

Return ONLY valid JSON.

{
  "signal_assessment": "...",
  "risk_interpretation": "...",
  "confidence": 0-10
}
"""

        user_prompt = f"""
Signals: {signals}
Deviations: {deviations}
"""

        cognition = LLMClient.reason(system_prompt, user_prompt, "TrendAgent")

        return cognition
