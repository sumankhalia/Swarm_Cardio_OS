from utils.llm_client import LLMClient


class StabilityAgent:

    @staticmethod
    def evaluate(signals, composite_score):

        system_prompt = """
You are StabilityAgent inside a cardiac cognitive AI swarm.

Role:
Evaluates buffering capacity, resilience, recovery balance.

CRITICAL RESPONSE RULES:

- Return ONLY valid JSON
- No verbosity
- No formatting
- No advice tone

Required JSON Format:

{
  "signal_assessment": "stability-oriented interpretation",
  "risk_interpretation": "stability implications",
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
            agent_name="StabilityAgent"
        )

        print("\n⚖ StabilityAgent Cognitive Interpretation")
        print("————————————————————")
        print(reasoning)

        return reasoning
