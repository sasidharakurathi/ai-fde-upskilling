import zipfile
from pathlib import Path
import httpx
import random

URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
DATA_DIR = Path("data/sms")
DATA_FILE = DATA_DIR / "SMSSpamCollection"

if not DATA_FILE.exists():    
    print("Downloading...")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    response = httpx.get(URL, timeout=60, follow_redirects=True)
    response.raise_for_status()
    zip_path = DATA_DIR / "sms.zip"
    zip_path.write_bytes(response.content)
    with zipfile.ZipFile(zip_path) as z:
        z.extract("SMSSpamCollection", DATA_DIR)
    print("Saved to", DATA_FILE)

labels = []
texts = []

for line in DATA_FILE.read_text(encoding="utf-8").split("\n"):
    if not line.strip():
        continue
    label, text = line.split("\t", 1)
    labels.append(label)
    texts.append(text)

print("Messages:", len(texts))

n_spam = labels.count("spam")
print("spam:", n_spam, "| ham:", labels.count("ham"), f"| spam share: {n_spam/len(labels):.1%}")

random.seed(42)

# for wanted in ["spam", "ham"]:
#     print(f"\n--- 3 {wanted} examples ---")
#     picks = [t for l, t in zip(labels, texts) if l == wanted]
#     for t in random.sample(picks, 3):
#         print("-", t[:100])

def features(text: str) -> dict:

    uppercase_count = sum(c.isupper() for c in text)

    return {
        "length": len(text),
        "digits": sum(c.isdigit() for c in text),
        "exclamations": text.count("!"),
        "uppercase": sum(c.isupper() for c in text),
        "has_free": 1 if "free" in text.lower() else 0,
        "has_http_or_www": 1 if ("http" in text.lower() or "www" in text.lower()) else 0,
        "capital_to_length_ratio": uppercase_count / len(text),
    }

# print("\n--- Turning a message into features (numbers) ---")
# print(texts[2])
# print(features(texts[2]))

def averages(wanted):
    rows = [features(t) for l, t in zip(labels, texts) if l == wanted]
    return {
        name: sum(r[name] for r in rows) / len(rows) for name in rows[0]
    }

spam_avg = averages("spam")
ham_avg = averages("ham")

print(f"\n{'feature':<30}{'spam':>8}{'ham':>8}")
for name in spam_avg:
    print(f"{name:<30}{spam_avg[name]:>8.2f}{ham_avg[name]:>8.2f}")