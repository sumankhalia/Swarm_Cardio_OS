from utils.llm_client import LLMClient


class StrategyAgent:

    @staticmethod
    def evaluate(signals, composite_score):

        system_prompt = """
You are StrategyAgent inside a cardiac cognitive AI swarm.

Role:
System-level strategic interpreter of physiological state.

CRITICAL RESPONSE RULES:

- Return ONLY valid JSON
- No markdown
- No bullet points
- No explanations
- No medical advice tone
- No extra text

Required JSON Format:

{
  "signal_assessment": "short systemic interpretation",
  "risk_interpretation": "strategic implication",
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
            agent_name="StrategyAgent"
        )

        print("\n🧠 StrategyAgent Cognitive Interpretation:")
        print(reasoning)

        return reasoning
