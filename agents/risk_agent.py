from utils.llm_client import query_llm

SYSTEM_PROMPT = """
You are the Risk Intelligence Agent inside a Cardiovascular Swarm Cognitive System.

Your role is to evaluate physiological vulnerability, instability probability, and acute cardiovascular stress signals.

You interpret signals conservatively and prioritize safety.

Avoid diagnosis or prescriptions.

Provide analytical reasoning in a cautious clinical risk assessment tone.
"""


class RiskAgent:

    @staticmethod
    def evaluate(signals):

        score = (
            signals["cardiac_load"] * 0.4
            + signals["autonomic_instability"] * 0.3
            + signals["hemodynamic_strain"] * 0.2
            + signals["fluid_retention_pressure"] * 0.1
        )

        if signals.get("event_flag"):
            score *= 1.3

        reasoning = query_llm(SYSTEM_PROMPT, signals, score)

        return score, reasoning
