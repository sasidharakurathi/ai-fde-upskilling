import joblib
from sklearn.tree import DecisionTreeClassifier
from sms_data import features, load_sms
from pathlib import Path

labels, texts = load_sms()
rows = [features(t) for t in texts]
names = list(rows[0])

X = [[row[n] for n in names] for row in rows]
y = labels

tree = DecisionTreeClassifier(max_depth=1)
tree.fit(X, y)

print("feature:", names[tree.tree_.feature[0]], "| threshold:", tree.tree_.threshold[0])
print(f"accuracy: {tree.score(X, y):.1%}")

joblib.dump(tree, "data/models/stump.joblib")

# new = ["Call me at 07123456789 when you land", "Are we still meeting for lunch tomorrow?"]
# new = [
#     "WINNER!! You have won a 1000 prize. Call 09061701461 now to claim",
#     "Are we still meeting for lunch tomorrow?",
#     "Call me at 07123456789 when you land",     # tricky: a normal message, but with a phone number
#     "FREE FREE FREE click here",                # tricky: spammy, but no digits
#     "",                                          # tricky: an empty message
# ]
new = new_messages = Path("data/my_messages.txt").read_text(encoding="utf-8").splitlines()
print(tree.predict([[features(t)[n] for n in names] for t in new]))