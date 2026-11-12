import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

my_api_key = os.environ.get("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API KEY not found.")

client = Groq(api_key = my_api_key)



model = "openai/gpt-oss-120b"

messages = [{"role": "user", "content": "What is AI?"}]

response = client.chat.completions.create(model = model, messages = messages)

print(response.choices[0].message.content)

