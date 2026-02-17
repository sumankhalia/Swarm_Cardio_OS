from utils.llm_client import query_llm

SYSTEM_PROMPT = """
You are the Physiological Instability Detection Agent.

Detect silent deterioration and resilience erosion patterns.
"""


class InstabilityAgent:

    @staticmethod
    def evaluate(signals):

        score = signals["variability_risk"]

        reasoning = query_llm(SYSTEM_PROMPT, signals, score)

        return reasoning
