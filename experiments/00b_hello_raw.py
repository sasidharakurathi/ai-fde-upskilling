from dotenv import load_dotenv
import os
import httpx

load_dotenv()

claude_api_key = os.environ.get("ANTHROPIC_API_KEY")
claude_model = os.environ.get("CLAUDE_MODEL")


# PROMPT = "Explain what an API is in two sentences."
PROMPT = "Explain how Push Down Automata works in detail"
INPUT_PRICE = 0.0
OUTPUT_PRICE = 0.0

print("Model: ", claude_model)

url = "https://api.anthropic.com/v1/messages"

headers = {
    "x-api-key": claude_api_key,
    "anthropic-version": "2026-10-21",
    "content-type": "application/json",
}

body = {
    "model": claude_model,
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": PROMPT},
    ],
}

response = httpx.post(url, headers=headers, json=body, timeout=60)
# print("Status coed: ", response.status_code)

if response.status_code != 200:
    print(response.text)
    raise SystemExit(1)

import json
data = response.json()
# print(json.dumps(data, indent=2))

print("Stop reason:", data["stop_reason"])
print("Input tokens:", data["usage"]["input_tokens"])
print("Output tokens:", data["usage"]["output_tokens"])

for block in data["content"]:
    if block["type"] == "text":
        print("Response:", block["text"])

cost = (data["usage"]["input_tokens"] * (4.00 / 1_000_000)) + (data["usage"]["output_tokens"] * (20.00 / 1_000_000))

print(f"Total Cost: ${cost:.5f}")