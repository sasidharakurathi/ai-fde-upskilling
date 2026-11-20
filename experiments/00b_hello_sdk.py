import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

claude_model = os.environ.get("CLAUDE_MODEL")

PROMPT = "Explain what an API is in two sentences."
# PROMPT = "Explain how Push Down Automata works in detail"
INPUT_PRICE = 0.0
OUTPUT_PRICE = 0.0

client = anthropic.Anthropic()
try:
    response = client.messages.create(
        model=claude_model,
        max_tokens=1024,
        messages=[{"role": "user", "content": PROMPT}],
    )
except anthropic.APIStatusError as e:
    print("API error: ", e.status_code, e.message)
    raise SystemExit(1)

# print(response)

print("Stop reason:", response.stop_reason)
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)

for block in response.content:
    if block.type == "text":
        print(block.text)

cost = (response.usage.input_tokens * (4.00 / 1_000_000)) + (response.usage.output_tokens * (20.00 / 1_000_000))

print(f"Total Cost: ${cost:.5f}")