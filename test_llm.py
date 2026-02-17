from utils.llm_client import LLMClient

system = "You are a test agent. Respond with a short sentence."
user = "Say hello."

result = LLMClient.reason(system, user)

print(result)
