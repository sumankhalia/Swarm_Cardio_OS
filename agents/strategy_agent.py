from utils.llm_client import query_llm

SYSTEM_PROMPT = """
You are the Strategy Intelligence Agent inside a Cardiovascular Swarm Cognitive System.

Your role is to evaluate adaptive capacity, resilience potential, and physiological coping ability.

You interpret signals through the lens of long-term stability, recovery strength, variability tolerance, and systemic adaptation.

You deliberately avoid diagnosis or medical prescriptions.

Provide analytical reasoning in a professional clinical intelligence tone.
"""


class StrategyAgent:

    @staticmethod
    def evaluate(signals):

        score = (
            signals["cardiac_load"] * 0.35
            + signals["recovery_deficit"] * 0.25
            + signals["autonomic_instability"] * 0.25
            + signals["variability_risk"] * 0.15
        )

        reasoning = query_llm(SYSTEM_PROMPT, signals, score)

        return score, reasoning
