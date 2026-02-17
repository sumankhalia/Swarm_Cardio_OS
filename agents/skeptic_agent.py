from utils.llm_client import query_llm

SYSTEM_PROMPT = """
You are the Skeptic Intelligence Agent inside a Cardiovascular Swarm Cognitive System.

Your role is to challenge assumptions and detect contradictions.
"""


class SkepticAgent:

    @staticmethod
    def evaluate(strategy_score, risk_score):

        score = abs(strategy_score - risk_score)

        reasoning = query_llm(
            SYSTEM_PROMPT,
            {"strategy_score": strategy_score, "risk_score": risk_score},
            score
        )

        return score, reasoning
