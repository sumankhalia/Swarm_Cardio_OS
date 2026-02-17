from utils.llm_client import query_llm

SYSTEM_PROMPT = """
You are the Governance Intelligence Agent inside a Cardiovascular Swarm Cognitive System.

Your role is to evaluate regulatory balance and behavioral stability.

Focus on sleep-stress regulation dynamics.
"""


class GovernanceAgent:

    @staticmethod
    def evaluate(signals):

        score = (
            signals["sleep_quality"] * 0.6
            + (10 - signals["stress_index"]) * 0.4
        )

        reasoning = query_llm(SYSTEM_PROMPT, signals, score)

        return score, reasoning
