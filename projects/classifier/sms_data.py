
import zipfile
from pathlib import Path
import httpx

URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
DATA_DIR = Path("data/sms")
DATA_FILE = DATA_DIR / Path("SMSSpamCollection")

def download_if_needed():
    if DATA_FILE.exists():
        return
    print("Downloading...")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    response = httpx.get(URL, timeout=60, follow_redirects=True)
    response.raise_for_status()
    zip_path = DATA_DIR / "sms.zip"
    zip_path.write_bytes(response.content)
    with zipfile.ZipFile(zip_path) as z:
        z.extract("SMSSpamCollection", DATA_DIR)
    print("Saved to", DATA_FILE)

def load_sms():
    download_if_needed()
    labels, texts = [], []
    for line in DATA_FILE.read_text(encoding="utf-8").split("\n"):
        if not line.strip():
            continue
        label, text = line.split("\t", 1)
        labels.append(label)
        texts.append(text)
    return labels, texts

def features(text: str) -> dict:

    uppercase_count = sum(c.isupper() for c in text)

    return {
        "length": len(text),
        "digits": sum(c.isdigit() for c in text),
        "exclamations": text.count("!"),
        "uppercase": sum(c.isupper() for c in text),
        "has_free": 1 if "free" in text.lower() else 0,
        "has_http_or_www": 1 if ("http" in text.lower() or "www" in text.lower()) else 0,
        "capital_to_length_ratio": uppercase_count / len(text) if text else 0.0,
    }