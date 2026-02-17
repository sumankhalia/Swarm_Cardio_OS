import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class LLMClient:

    MODEL = "gpt-4.1-mini"

    @staticmethod
    def reason(system_prompt, user_prompt, agent_name="Agent"):

        try:
            response = client.responses.create(
                model=LLMClient.MODEL,
                input=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                max_output_tokens=200
            )

            text_output = response.output[0].content[0].text

            print(f"\n{agent_name} Cognitive Interpretation")
            print("—" * 20)
            print(text_output)

            return json.loads(text_output)

        except Exception as e:

            print(f"\n⚠ {agent_name} cognition fallback triggered")

            return {
                "signal_assessment": "Cognitive interpretation unavailable",
                "risk_interpretation": "Fallback reasoning engaged",
                "confidence": 0
            }
