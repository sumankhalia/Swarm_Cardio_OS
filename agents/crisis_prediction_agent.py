from utils.llm_client import LLMClient


class CrisisPredictionAgent:

    @staticmethod
    def evaluate(signals, deviations):

        system_prompt = """
You are CrisisPredictionAgent inside a cardiac cognitive AI swarm.

Role:
Estimates near-term destabilization probability using deviations.

CRITICAL RESPONSE RULES:

- Return ONLY valid JSON
- No long explanations
- No markdown
- No clinical advice style

Required JSON Format:

{
  "signal_assessment": "crisis-relevant deviation reading",
  "risk_interpretation": "crisis probability implication",
  "confidence": 0-10
}
"""

        user_prompt = f"""
Signals: {signals}
Deviations: {deviations}
"""

        reasoning = LLMClient.reason(
            system_prompt,
            user_prompt,
            agent_name="CrisisPredictionAgent"
        )

        return reasoning
