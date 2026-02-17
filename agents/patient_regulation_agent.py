from utils.llm_client import LLMClient


class PatientRegulationAgent:

    system_prompt = """
    You are PatientRegulationAgent inside a cardiac cognitive AI swarm.

    Role:
    Translate physiological risk patterns into stabilizing behavioral guidance.

    CRITICAL RESPONSE RULES:

    - Return ONLY valid JSON
    - No medical diagnosis
    - No medication suggestions
    - No clinical treatment language
    - No markdown
    - No bullet points
    - No alarming tone

    Required JSON Format:

    {
      "signal_assessment": "physiological self-regulation interpretation",
      "regulation_focus": "dominant stabilization priorities",
      "adaptive_guidance": "safe lifestyle / behavioral adjustments",
      "confidence": 0-10
    }
    """

    @staticmethod
    def evaluate(signals, composite_score):

        user_prompt = f"""
        Signals: {signals}
        Composite Score: {composite_score}
        """

        reasoning = LLMClient.reason(
            PatientRegulationAgent.system_prompt,
            user_prompt,
            "PatientRegulationAgent"
        )

        return reasoning
