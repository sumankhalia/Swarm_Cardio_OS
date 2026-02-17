from utils.llm_client import LLMClient


class GovernanceAgent:

    @staticmethod
    def evaluate(signals, composite_score):

        system_prompt = """
You are GovernanceAgent inside a cardiac cognitive AI swarm.

Role:
Evaluates regulatory balance, intervention necessity, control priorities.

CRITICAL RESPONSE RULES:

- Return ONLY valid JSON
- No policy explanations
- No markdown
- No recommendations phrasing

Required JSON Format:

{
  "signal_assessment": "regulatory stability reading",
  "risk_interpretation": "governance implication",
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
            agent_name="GovernanceAgent"
        )

        print("\nGovernanceAgent Cognitive Interpretation")
        print("————————————————————")
        print(reasoning)

        return reasoning
