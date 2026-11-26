# Lesson Notes (revision sheet)

Short notes for every finished lesson, written by Claude from **your own code and results**. Come back here when
you need a refresher. The full explanations are in `lessons/`.

---

## Stage 0 · The big map ✅

### 0.1 · AI vs ML vs Deep Learning vs Generative AI vs LLMs
- **Circles inside circles:** AI ⊃ Machine Learning ⊃ Deep Learning ⊃ Generative AI ⊃ LLMs.
- **AI** = computers doing tasks that need thinking. There are four ways to do it:
  | Way | Knowledge comes from | Example |
  |-----|----------------------|---------|
  | Rules | A human writes if-then rules | A bank flags transfers over $10,000 |
  | Search / planning | The computer tries options until a goal is met | Google Maps route, Sudoku solver, exam timetable |
  | Logic / knowledge | Facts plus reasoning | "Alice manages Platform" → "Alice's team follows its policy" |
  | **Machine Learning** | **Learned from examples** | Spam filter, face unlock, Claude |
- **Deep learning** = ML with neural networks, good at raw data (images, sound, text). **Generative AI** = creates new
  content. **LLM** = generative AI for text, trained to predict the next token. Many LLMs can also *read* images.
- **Model** = the learned numbers (patterns), **not** the training data. **Training** = learning them. **Inference** = using them.
- An LLM doesn't search the web by itself. The **app** runs a search tool and puts the results in the prompt.

### 0.2 · AI Engineer vs Forward Deployed Engineer
- **AI Engineer:** builds the AI system (RAG, agents, prompts, model choice, **evals**). Success = measurably good.
- **FDE:** makes it work **inside a customer's world** (their data, SSO login, security review, network, demos,
  honest limits). Success = the customer gets real value.
- **Both:** Python, building RAG, evals, debugging, deployment basics, security awareness, clear writing.
- **Honesty about limits:** "It's right about 90% of the time, so a person should check important answers" protects
  the customer and builds trust. Over-promising leads to real harm, lost trust, and lost contracts.
- **Researcher** invents new methods · **ML Engineer** trains/runs custom models · **AI Engineer** builds with existing models.
- *Your first role signal:* the most fun tasks were testing prompts, comparing models, designing agents, and building RAG (AI-Engineer-flavoured).

### 0.3 · The parts of an AI app
- **Flow:** ① UI → ② backend code (checks login) → ③ data / retrieval → ④ prompt (instructions + found text + history +
  question) → ⑤ model → ⑥ output checks (guardrails) → back to the user. ⑦ Logs + evals run in the background.
- **The model is stateless:** each call starts fresh. Chat apps "remember" because the code **re-sends the history**,
  so long chats cost more tokens.
- **Wrong answer? Check the cheap things first:** out-of-date data, retrieval found the wrong text, the prompt, the code
  (e.g. missing permission check). Then the model.
- **Layers of safety:** the prompt tries to prevent a problem; a guardrail catches it if it happens anyway; best of all,
  never give the model data it shouldn't use.

### 0.4a · Workspace, secrets, git habits
- **Virtual environment (`.venv`)** = one toolbox of packages per project. `uv init` / `uv add` / `uv run`.
- `pyproject.toml` = shopping list; `uv.lock` = exact receipt. Commit both. **Never commit `.venv/` or `.env`.**
- **Secrets** live in `.env` (listed in `.gitignore`) and are read via environment variables.
  **Leaked key → revoke it first**, then clean up. Deleting the commit isn't enough.
- **Your result:** your own `.env` reader handled quotes and trailing comments. Tricky lines it didn't handle (the lesson
  didn't ask for them): no `#` on the line, blank lines, `=` inside a value, `#` inside quotes.
  `python-dotenv` handles all of them. **That's what a package hides: the edge cases.**
- **How to find edge cases:** what if it's *missing*, *empty*, has *extra spaces*, or contains the *special characters* my code looks for?

### 0.4b · First LLM call (raw HTTP, then the SDK)
- **Request:** `POST https://api.anthropic.com/v1/messages`. Headers: `x-api-key` (who you are and who pays),
  `anthropic-version: 2026-10-21` (API rules version), `content-type: application/json`. Body: `model`, `max_tokens`, `messages`.
- **Response:** `content` is a **list of blocks** (pick out `type == "text"`; there may be a `thinking` block first),
  `stop_reason` (`end_turn` = finished; `max_tokens` = **cut off**), `usage` (input/output tokens).
- **Cost** = `input_tokens × in_price/1M + output_tokens × out_price/1M`. Output costs more, and thinking counts as output.
- **Status codes:** 200 OK · 4xx your mistake (401 key, 400/404 body or model) · 5xx/529 their side.
- **SDK vs raw:** your raw script was **55 lines**, the SDK one **37**. The SDK hid the URL, headers, API version, raw JSON,
  and automatic retries, and it **raises** typed errors that you catch (`except anthropic.APIStatusError as e`).
  Raw printed the 401 JSON; the SDK printed `API error: 401 ...`.
- **Tips from your code:** use your price variables instead of typing numbers into the formula. `os.environ["X"]` **fails fast**
  on missing config; `.get()` hides the problem until later.
- **Model IDs live in `.env` (`CLAUDE_MODEL`)**, not in code. Treat them as config.

---

## Stage 1 · How machines learn 🔵

### 1.1 · Data, features, labels
- **Example** = one message · **Label** = the right answer (spam/ham) · **Feature** = a **number** describing the
  example. A model only ever sees the numbers.
- **Look at the data first.** 5,574 messages, **747 spam (13.4%)**. Imbalanced: "always ham" is already 86.6% "right".
- **Your feature table** (averages):
  | feature | spam | ham | clue? |
  |---------|-----:|----:|-------|
  | digits | 15.81 | 0.31 | **strongest** (about 50× more in spam) |
  | uppercase | 15.47 | 4.11 | strong |
  | length | 138.68 | 71.47 | strong |
  | has_free | 0.27 | 0.01 | good |
  | has_http_or_www *(yours)* | 0.14 | 0.00 | good: almost never in normal messages |
  | exclamations | 0.73 | 0.18 | medium |
  | capital_to_length_ratio *(yours)* | 0.11 | 0.06 | weak |
- **Tricky input met:** the file ends with an empty line, so a naive `split("\t")` crashes. Skip blank lines.
- **Your loader vs Hugging Face `datasets`:**
  | | Yours | `datasets` |
  |---|---|---|
  | Count | 5,574 | 5,574 |
  | Label | `"ham"` / `"spam"` (text) | `0` / `1` (numbers: **label encoding**; `ds.features["label"]` maps them back) |
  | Text | as in the file | **adds `\n` to the end of every message** |
  | Order | same | same |
  | Stored in | `data/sms/` | the Hugging Face **cache** (`~/.cache/huggingface/`) |
  It hid the download, the caching, the label mapping, and an extra character. *A lesson for the coach too:* 187
  messages end with a space, and a careless comparison (stripping only one side) made them look different when they weren't.
  **When comparing two versions, compare them the same way.**

### 1.2 · Training vs inference: your first model
- **Model** = a few **learned numbers**. Yours is 2 values in `data/models/stump.json`: `{"feature": "digits", "threshold": 5}`.
- **Training** = searching for the numbers with the **fewest mistakes** on labelled data (`mistakes()` + loop over every
  feature and threshold). **Inference** = applying them to new messages (`predict.py`). No labels, no learning.
- **This is supervised learning:** `if guess != truth` only works because every message has a label.
  More precisely, it's **supervised classification** (the label is a category).
- **Your result:** best rule = **digits** (149 mistakes, **97.3%**). The best "length" rule made 747 mistakes = "say ham to
  everything" = **86.6%**. That's the **baseline** to beat.
- **Decision stump** = a 1-question **decision tree**. scikit-learn's `DecisionTreeClassifier(max_depth=1)` found the same
  line (`digits <= 4.5`), the same 97.3%. `.fit(X, y)` = train, `.predict(...)` = inference. `X` = features table, `y` = labels.
- **Majority vote at each leaf:** the "digits > 4.5" side has 648 spam / 50 ham → answer spam; the other side has
  4,777 ham / 99 spam → answer ham. The losers are the mistakes: 50 + 99 = 149.
- **Impurity (Gini):** how *mixed* a side is (all one label = 0, 50/50 = worst). Trees pick the least-mixed split.
- **Combining features** (measured on 25% of messages the models never saw):
  | Model | Train acc | **New-message acc** |
  |---|---:|---:|
  | 1 question | 97.3% | 97.3% |
  | 3 questions | 97.8% | **97.8%** |
  | 10 questions | 99.5% | 97.3% |
  | no limit | 99.9% | 97.1% |
  The 2nd question the tree picks is **your** `has_http_or_www`. A little combining helps; too much = **memorising**
  (overfitting, Lesson 1.4). Bigger gains need **better features** (e.g. the words themselves).
- **Your Gmail test (distribution shift):** the SMS model got most of your email subjects **wrong**. It missed all 5
  promotions (no phone numbers) and flagged order emails as spam ("Order Placed (ID: 21687135)" has 8 digits). A model
  only knows the kind of data it learned from. Real-world data that looks different = **distribution shift**.
  This is a core FDE problem. Personal and customer data stays in `data/` (gitignored), never in code.
- **🐞 Bug you found (by doing the ✋ your-turn):** `train_stump.py` trains with `>=` (saved `threshold: 5`), but `predict.py`
  applies `>`. A message with exactly 5 digits (39 training messages, 28 of them spam) is spam in training but ham in
  prediction. scikit-learn's model says spam for "order #27877", yours says ham. **Training and inference must apply
  exactly the same rule.** When they don't, it's called **training-serving skew**, a classic production bug. Fix: save the
  rule in the model file (e.g. `"rule": ">="`), or put the rule in one shared function both scripts import.

### 1.3a · Kinds of learning, and finding similar messages
- **Kinds of learning:** supervised (labels: your stump) · unsupervised (no labels: similarity, groups) · self-supervised
  (the label is hidden in the data, e.g. the next word, which is how LLMs train) · reinforcement (actions + rewards).
- **Vector** = a message's features as a list of numbers. **Euclidean distance** = √(sum of squared differences); small = similar.
- **`nearest()`** sorts the *positions* 0…5573 by their distance to the query and keeps the first k (positions let you look up `texts[i]`, `labels[i]`).
- **Without scaling, `length` (range 2–910) drowns out `has_free` (0–1)**, so the "similar" messages were just similar
  in length. **Min-max scaling** to 0–1 fixed it: the WINNER query's neighbours all share FREE and WIN (distances 0.192, 0.196, 0.208).
- **No labels were used to search.** Peeking afterwards: spam queries found spam, normal queries found normal messages.
- **Your tricky queries:**
  | Query | What happened | Why |
  |---|---|---|
  | `""` (empty) | scaled length = **−0.002** | the shortest message in the data is `"Ok"` (2 chars); scaling uses the data's min/max |
  | `"a" * 2000` | scaled length = **2.2** | longer than the longest message (910): values can land outside 0–1 |
  | `texts[0]` (exact copy) | **3 neighbours at distance 0.000** | itself, plus 2 *different* messages with identical features |
- **Big finding:** your 7 features give only **2,388 different vectors for 5,574 messages**, and 3,883 messages share their
  exact numbers with another message. "Go until jurong point…" and "Ok good then i later come find ü…" look identical to
  the model. **Hand-made features are blind to meaning.** That's why later stages use **embeddings** (vectors that capture
  meaning) for similarity search and RAG.
- **scikit-learn:** `MinMaxScaler` (`fit_transform` on data, `transform` only on new queries) + `NearestNeighbors` gave
  **identical** neighbours, distances, and mins/maxs. **Scale new data with the training data's numbers**: calling `fit` on
  new data is the scaling version of the `>=`/`>` bug from 1.2.
