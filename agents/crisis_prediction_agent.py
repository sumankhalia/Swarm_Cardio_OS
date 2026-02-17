from utils.llm_client import query_llm


SYSTEM_PROMPT = """
You are the Crisis Prediction Intelligence Agent.

Estimate probability of future cardiovascular instability.
"""


class CrisisPredictionAgent:

    @staticmethod
    def evaluate(signals, deviations):

        score = (
            signals["cardiac_load"]
            + signals["autonomic_instability"]
            + abs(deviations.get("cardiac_load", 0))
        ) / 3

        reasoning = query_llm(
            SYSTEM_PROMPT,
            {"signals": signals, "deviations": deviations},
            score
        )

        return reasoning
