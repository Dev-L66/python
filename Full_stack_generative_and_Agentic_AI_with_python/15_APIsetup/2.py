import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

my_api_key = os.environ.get("GEMINI_API_KEY")
my_base_url = os.environ.get("BASE_URL")

if not my_api_key:
    raise ValueError("API KEY not found.")

client = OpenAI(api_key = my_api_key, base_url = my_base_url)

model = "gemini-3.5-flash"

messages = [{"role": "user", "content": "What is AI? Explain in 5-10 sentences only."}]

response = client.chat.completions.create(model=model, messages=messages)

print(response.choices[0].message.content)