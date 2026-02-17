from utils.llm_client import query_llm

SYSTEM_PROMPT = """
You are the Trend Intelligence Agent.

Evaluate directional drift and progressive deterioration signals.
"""


class TrendAgent:

    @staticmethod
    def evaluate(history):

        score = len(history)  # placeholder metric

        reasoning = query_llm(
            SYSTEM_PROMPT,
            {"history_length": len(history)},
            score
        )

        return reasoning
