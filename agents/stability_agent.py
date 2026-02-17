from utils.llm_client import query_llm

SYSTEM_PROMPT = """
You are the Stability Intelligence Agent inside a Cardiovascular Swarm Cognitive System.

Your role is to evaluate buffering capacity, resilience integrity, and recovery strength.

Provide calm physiological stability reasoning.
"""


class StabilityAgent:

    @staticmethod
    def evaluate(signals):

        score = (
            10
            - signals["recovery_deficit"] * 0.6
            - signals["variability_risk"] * 0.4
        )

        reasoning = query_llm(SYSTEM_PROMPT, signals, score)

        return score, reasoning
