from utils.llm_client import LLMClient


class InstabilityAgent:

    @staticmethod
    def evaluate(signals, composite_score):

        system_prompt = """
You are InstabilityAgent inside a cardiac cognitive AI swarm.

Role:
Detects deterioration patterns, strain accumulation, collapse dynamics.

CRITICAL RESPONSE RULES:

- Return ONLY valid JSON
- No essays
- No bullet points
- No dramatic language

Required JSON Format:

{
  "signal_assessment": "instability pattern reading",
  "risk_interpretation": "destabilization implication",
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
            agent_name="InstabilityAgent"
        )

        print("\nInstabilityAgent Cognitive Interpretation")
        print("————————————————————")
        print(reasoning)

        return reasoning
