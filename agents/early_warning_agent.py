from utils.llm_client import query_llm

SYSTEM_PROMPT = """
You are the Early Warning Intelligence Agent.

Estimate future instability probability and crisis likelihood.
"""


class EarlyWarningAgent:

    @staticmethod
    def evaluate(signals):

        score = (
            signals["cardiac_load"]
            + signals["autonomic_instability"]
            + signals["fluid_retention_pressure"]
        ) / 3

        reasoning = query_llm(SYSTEM_PROMPT, signals, score)

        return reasoning
