from utils.llm_client import LLMClient


class RiskAgent:

    @staticmethod
    def evaluate(signals, composite_score):

        system_prompt = """
You are RiskAgent inside a cardiac cognitive AI swarm.

Role:
Quantifies vulnerability and destabilization probability.

CRITICAL RESPONSE RULES:

- Return ONLY valid JSON
- No explanations
- No markdown
- No clinical narrative
- No extra words

Required JSON Format:

{
  "signal_assessment": "risk-relevant signal reading",
  "risk_interpretation": "risk trajectory meaning",
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
            agent_name="RiskAgent"
        )

        print("\n📉 RiskAgent Cognitive Interpretation:")
        print(reasoning)

        return reasoning
