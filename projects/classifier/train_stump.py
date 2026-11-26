import json
from pathlib import Path

from sms_data import load_sms, features

labels, texts = load_sms()

rows = [features(t) for t in texts]
is_spam = [label=="spam" for label in labels]

def mistakes(feature_name, threshold):
    count = 0
    for row, truth in zip(rows, is_spam):
        # guess = row[feature_name] > threshold
        guess = row[feature_name] >= threshold
        if guess != truth:
            count += 1
    return count

# print("Digit Mistakes:", mistakes("digits", 4)) # Got: 149
# print("http or www Mistakes:", mistakes("has_http_or_www", 0)) # Got: 643
# print("Has free Mistakes:", mistakes("has_free", 0)) # Got: 614
# print("Caps to length ratio Mistakes:", mistakes("capital_to_length_ratio", 0.5)) # Got: 844

best = None
for name in rows[0]:
    values = sorted(set(row[name] for row in rows))
    if len(values) > 100:
        values = values[:: len(values) // 100]
    for threshold in values:
        m = mistakes(name, threshold)
        if best is None or m < best["mistakes"]:
            best = {"feature": name, "threshold": threshold, "mistakes": m}
    print(f"tried {name:<25} best so far: {best['feature']} > {best['threshold']} ({best['mistakes']} mistakes)")

accuracy = 1 - best["mistakes"] / len(rows)
print(f"\nModel: spam if {best['feature']} > {best['threshold']}  ->  {best['mistakes']} mistakes, accuracy {accuracy:.1%}")

model = {"feature": best["feature"], "threshold": best["threshold"]}
Path("data/models").mkdir(parents=True, exist_ok=True)
Path("data/models/stump.json").write_text(json.dumps(model, indent=2))
print("Saved: ", model)