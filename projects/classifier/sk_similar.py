from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler

from sms_data import features, load_sms

labels, texts = load_sms()
names = list(features("x"))
X = [[features(t)[n] for n in names] for t in texts]

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
nn = NearestNeighbors(n_neighbors=3).fit(X_scaled)

queries = ["WINNER!! Call 09061701461 now to claim your FREE prize www.win.com", "ok see you soon", ""]
q_scaled = scaler.transform([[features(q)[n] for n in names] for q in queries])
distances, indices = nn.kneighbors(q_scaled)
for q, ds, ids in zip(queries, distances, indices):
    print("\nQUERY:", repr(q))
    for d, i in zip(ds, ids):
        print(f"  {labels[i]:<5} d={d:.3f}  {texts[i][:70]}")
print("\nscaler min:", scaler.data_min_)
print("scaler max:", scaler.data_max_)