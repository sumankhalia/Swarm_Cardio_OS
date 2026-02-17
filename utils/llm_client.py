from openai import OpenAI
from utils.env_loader import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def query_llm(system_prompt, signals, score):

    prompt = f"""
    {system_prompt}

    Signals:
    {signals}

    Computed Score: {round(score, 2)}

    Provide analytical reasoning.
    Do not diagnose.
    """

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content
