from utils.llm_client import LLMClient


class SkepticAgent:

    @staticmethod
    def evaluate(signals, composite_score):

        system_prompt = """
You are SkepticAgent inside a cardiac cognitive AI swarm.

Role:
Challenges assumptions, detects contradictions, evaluates uncertainty.

CRITICAL RESPONSE RULES:

- Return ONLY valid JSON
- No philosophical essays
- No markdown
- No verbose critique

Required JSON Format:

{
  "signal_assessment": "uncertainty / contradiction reading",
  "risk_interpretation": "confidence limitation",
  "confidence": 0-10
}
"""

        user_prompt = f"""
Signals: {signals}
Composite Score: {composite_score}
"""

        reasoning = LLMClient.reason(
            system_prompt,
            user_prompt,
            agent_name="SkepticAgent"
        )

        return reasoning
