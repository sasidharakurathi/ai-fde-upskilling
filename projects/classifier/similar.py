import math
from sms_data import features, load_sms

labels, texts = load_sms()

rows = [features(t) for t in texts]
names = list(rows[0])

vectors = [[row[n] for n in names] for row in rows]
print(names)
print(texts[0][:60], vectors[0])

def distance(a, b):
    return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))

# print(distance([100, 12], [20, 0]))

def nearest(query_vector, vecs, k=3):
    order = sorted(range(len(vecs)), key=lambda i: distance(query_vector, vecs[i]))
    return order[:k]

queries = [
    "WINNER!! Call 09061701461 now to claim your FREE prize www.win.com",
    "ok see you soon",
    "",
    "a" * 2000,
    texts[0]
]
# for q in queries:
#     qv = [features(q)[n] for n in names]
#     print("\nQUERY:", q)
#     for i in nearest(qv, vectors):
#         print(f"  {labels[i]:<5} d={distance(qv, vectors[i]):6.1f}  {texts[i][:70]}")

mins = [min(col) for col in zip(*vectors)]
maxs = [max(col) for col in zip(*vectors)]
print("mins", mins)
print("maxs", maxs)

def scale(v):
    return [(x - lo) / (hi - lo) if hi > lo else 0.0 for x, lo, hi in zip(v, mins, maxs)]

scaled = [scale(v) for v in vectors]

for q in queries:
    qv = scale([features(q)[n] for n in names])
    print("\nQUERY:", q)
    for i in nearest(qv, scaled):
        print(f"  {labels[i]:<5} d={distance(qv, scaled[i]):6.3f}  {texts[i][:70]}")
