
import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

print("Models available for text generation:\n")

for model in client.models.list():
    actions = getattr(model, "supported_actions", []) or []

    if "generateContent" in actions:
        print(model.name)
