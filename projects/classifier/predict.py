import json
from pathlib import Path

from sms_data import features

model = json.loads(Path("data/models/stump.json").read_text())

# new_messages = [
#     "WINNER!! You have won a 1000 prize. Call 09061701461 now to claim",
#     "Are we still meeting for lunch tomorrow?",
#     "Call me at 07123456789 when you land",     # tricky: a normal message, but with a phone number
#     "FREE FREE FREE click here",                # tricky: spammy, but no digits
#     "",                                          # tricky: an empty message
# ]

new_message = new_messages = Path("data/my_messages.txt").read_text(encoding="utf-8").splitlines()

for text in new_messages:
    value = features(text)[model["feature"]]
    guess = "spam" if value > model["threshold"] else "ham"
    print(f"{guess:<5} ({model['feature']}={value})  {text!r}")