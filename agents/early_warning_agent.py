from utils.llm_client import LLMClient


class EarlyWarningAgent:

    @staticmethod
    def evaluate(signals, deviations):

        system_prompt = """
You are EarlyWarningAgent inside a cardiac cognitive AI swarm.

Role:
Detects emerging risk signals before crisis thresholds.

CRITICAL RESPONSE RULES:

- Return ONLY valid JSON
- No alarmist language
- No explanations

Required JSON Format:

{
  "signal_assessment": "early deviation reading",
  "risk_interpretation": "forward-looking implication",
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
            agent_name="EarlyWarningAgent"
        )

        return reasoning
