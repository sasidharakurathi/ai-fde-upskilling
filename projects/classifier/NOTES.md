# P1 · Classifier: notes and comparisons

*Written by Claude from running your code. Revision notes for each lesson: `notes/lesson-notes.md`.*

## Compare (1.1): own loader ① vs Hugging Face `datasets` ②
| Test | ① `01_explore.py` | ② `02_load_with_datasets.py` |
|------|-------------------|------------------------------|
| Messages | 5,574 | 5,574 |
| Label | `"ham"` / `"spam"` | `0` / `1` (label encoding; names in `ds.features["label"]`) |
| First message identical? | — | **No**: `datasets` adds `\n` to the end of every message |
| Same order? | — | Yes |
| Where stored | `data/sms/` (you chose) | Hugging Face cache (`~/.cache/huggingface/`) |
| Lines of code | ~35 for loading | 3 |

**What `datasets` did for you:** download, unzip, parse, cache, and label encoding.
**What it hid:** where the file lives, the label-to-number mapping, and the extra `\n` it adds.
**At work:** `datasets` for well-known public datasets; your own loader for a **customer's** files, which are never on
Hugging Face and are always messy.

## Compare (1.2): own stump ① vs scikit-learn `DecisionTreeClassifier(max_depth=1)` ②
Same 5,574 messages, same 7 features.
| | ① `train_stump.py` + `predict.py` | ② `sk_stump.py` |
|---|---|---|
| Learned rule | spam if digits **>= 5** (your `>=` experiment) | spam if digits **> 4.5** |
| Mistakes / accuracy | 149 / 97.3% | 149 / 97.3% |
| How a split is scored | count mistakes | Gini impurity (how mixed each side is) |
| Which side is spam | fixed: "above = spam" | majority vote per side |
| More questions | no | `max_depth=2, 3, …` |
| Model file | `stump.json` (2 readable values) | `stump.joblib` (binary Python object) |
| Training code | ~20 lines | 2 lines (`DecisionTreeClassifier(...)`, `.fit`) |

**Tricky inputs, both versions** (your `predict.py` with `>` vs `sk_stump.py`):
| Message | ① | ② | Note |
|---|---|---|---|
| "WINNER!! … Call 09061701461 …" | spam | spam | |
| "Are we still meeting for lunch tomorrow?" | ham | ham | |
| "Call me at 07123456789 when you land" | **spam** | **spam** | both wrong: digits ≠ spam here |
| "FREE FREE FREE click here" | **ham** | **ham** | both wrong: no digits |
| "" (empty) | ham | ham | |
| "A shipment from order #27877 is on the way" (5 digits) | **ham** | **spam** | ① trained with `>=` but predicts with `>`: **training-serving skew** |

**What scikit-learn hid:** the threshold search, impurity scoring, majority vote, and the model file format.
**At work:** scikit-learn (fast, tested, more questions with one setting). Your version is how you understand what it does,
and why the trained rule and the prediction rule must match.

## Compare (1.3a): own similarity search ① vs scikit-learn `MinMaxScaler` + `NearestNeighbors` ②
Same 5,574 messages, same 7 features, same queries.
| Query | ① `similar.py` (scaled) | ② `sk_similar.py` |
|---|---|---|
| "WINNER!! … FREE prize www.win.com" | 3 spam, d = 0.192 / 0.196 / 0.208 | **identical** |
| "ok see you soon" | 3 ham, d = 0.004 / 0.006 / 0.008 | **identical** |
| "" (empty) | ":)", ":-) :-)", ":-( sad puppy noise" | **identical** |
| mins / maxs | [2, 0, 0, 0, 0, 0, 0] / [910, 47, 11, 129, 1, 1, 1] | `data_min_` / `data_max_`: identical |

**Tricky inputs (① only):** empty → scaled length −0.002 · `"a" * 2000` → scaled length 2.2 · exact copy of a message →
3 neighbours at distance 0 (6 messages share those exact feature values).

**What scikit-learn did / hid:** scaling with stored min/max (`fit` vs `transform`), and a fast neighbour search
(your version compares the query with all 5,574 messages; `NearestNeighbors` can use smarter structures for millions of items).
**At work:** scikit-learn for these steps; for *meaning*-based similarity, embeddings + a vector database (Stage 5).

