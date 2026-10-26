# Learning Plan: AI Engineer and/or Forward Deployed Engineer

**Started:** Mon 2026-10-26 · **No deadlines.** You move forward when you pass each stage's **gate**.
**Starting point:** zero AI knowledge; coding (Python, APIs, git) is OK.
**Rough length:** 9–12 months at ~1 h on weekdays plus weekend sessions. That's only an estimate. Going
slow and steady is the plan, so it's not a problem.

---

## How this plan works

### The shape
```
FOUNDATIONS            BUILDING                     PRODUCTION + CUSTOMER          FINISH
Stage 0  The map       Stage 5  Search & RAG        Stage 11 LLMOps & safety       Stage 15 System design
Stage 1  How ML learns Stage 6  Evaluation          Stage 12 Cloud, network, auth  Stage 16 Specialize,
Stage 2  How LLMs work Stage 7  Shipping software   Stage 13 Multimodal                     portfolio,
Stage 3  Using LLMs    Stage 8  Knowledge graphs    Stage 14 FDE craft                      interviews
Stage 4  Data skills   Stage 9  Agents & MCP
                       Stage 10 Customizing models
                        ▲ role checkpoint after Stage 7
```

### Your week
| Day | Time | What happens |
|-----|------|--------------|
| Mon–Fri | ~1 h | **One lesson**: read (~20 min) → try it (~30 min) → explain it back (~10 min) → check in. |
| Saturday | 3–4 h | **Build**: the stage's practice project. |
| Sunday | ~45 min | Weekly review + quiz on anything due. Optional catch-up. |

A lesson can take 1, 2, or 3 days. **Slow is fine. Skipping is not.**

### How a lesson works
1. Claude writes the lesson file in `lessons/` (simple English, an everyday example, a small "try it").
2. You read it and do the "try it" part.
3. You answer the **"Explain it back"** questions in `notes/my-words.md`, **without looking**.
4. You tell Claude you're done. Claude checks your answers, corrects them gently, and writes the next lesson.

### Mastery gates (how you move to the next stage)
You pass a stage when **all three** are true:
1. Every lesson's explain-back is 🟩 solid or 🟨 shaky. **No 🟥 missing.**
2. The stage's project meets its **Done when**.
3. You pass a **gate quiz**: 3–5 mixed questions, at least 80% 🟩.

Not passing yet just means you repeat the weak lessons. That's normal and expected.

### Scratch → package: the rule for EVERY stage
Everything you build, you build up to **three ways**, in this order:

| Version | What it is | Why |
|---------|------------|-----|
| **① From scratch** | Your own code in plain Python + `numpy`. Small, maybe ugly. | So you *understand* how it works. |
| **② Local package / pretrained model** | Libraries and ready-made models you install with `pip` that **run on your machine**, e.g. `sentence-transformers` + `all-MiniLM-L6-v2`. Free to run, data stays with you, but uses your CPU/GPU. | So you can *work fast* with the tools teams actually use. |
| **③ Hosted API / managed service** | Someone else runs it; you call it over the internet, e.g. an embedding API like Voyage AI. Nothing to install, pay per use, **your data is sent to the provider**. | Because many companies use these, and FDEs must explain this trade-off to customers. |

A "—" in a stage's table means that version doesn't exist or isn't worth doing for that piece.
Stages 14–16 have no code, so there the rule becomes: **your own version first → a real-world template → compare**.

**How to compare (10–15 min, in the project's `NOTES.md`):** run every version on **the same test inputs**, then write:
1. **Results:** the numbers side by side (each stage's "Compare on" line says which ones).
2. **Speed and cost:** time per run; money per 1,000 runs (local = your hardware, hosted = the bill).
3. **Code:** lines of code, and how hard it was to debug something wrong.
4. **What the package hid** from you, which you only know because you built ①.
5. **Data:** where does the data go? (This decides many real customer projects.)
6. **Verdict:** which version you'd use at work, and when you'd pick a different one.

Each stage's **🧰 Scratch → package** table sits just above its gate. **Passing the gate needs every
version in that table** plus the comparison. This adds roughly 20–25% more time, which is worth it.
Model and service names change fast; the **stay-current track** keeps these tables fresh.

### Tags
- `[BOTH]`: needed for both roles. Never skip.
- `[AIE]`: deeper for AI Engineer.
- `[FDE]`: deeper for Forward Deployed Engineer.

Until the role checkpoint (after Stage 7), do everything. After it, do the `[BOTH]` lessons plus your
lean's lessons fully, and do the other lean's lessons in a lighter "know what it is" version.

---

## FOUNDATIONS

### Stage 0 · The big map `[BOTH]` · ~1 week
*Goal: know the words and the landscape, so nothing later sounds like magic.*
| # | Lesson |
|---|--------|
| 0.1 | AI vs Machine Learning vs Deep Learning vs Generative AI vs LLMs |
| 0.2 | What an AI Engineer does vs what an FDE does (a normal day for each) |
| 0.3 | The parts of an AI app: model, data, prompt, code, user (a simple tour) |
| 0.4 | Your workspace: Python with `uv`, `.env` and secrets, git habits, your first LLM API call |

**Project P0:** `experiments/00_hello_llm.py` sends one question to an LLM and prints the answer, the token
count, and the cost.

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Calling the LLM | Raw HTTP request with `httpx`: build the JSON body and headers yourself, read the raw response | — (a local LLM comes in Stages 2 and 10) | Official `anthropic` SDK calling the hosted Claude API *(the SDK is a local library, but the model runs on the provider's servers)* |
| Secrets | Read a `.env` file yourself with `os.environ` and a tiny parser | `python-dotenv` | A cloud secrets manager (Stage 12) |

**Compare on:** lines of code · what error handling and retries you got for free · what the raw request looks like (you'll debug with it later).

**Gate:** explain the AI → ML → DL → GenAI → LLM nesting with your own example of each.

### Stage 1 · How machines learn (ML basics) `[BOTH]`, deeper for `[AIE]` · ~2–3 weeks
*Goal: understand "learning from examples". Every later topic builds on this.*
| # | Lesson |
|---|--------|
| 1.1 | Data, features, and labels: what a computer "sees" |
| 1.2 | Training vs using a model (inference); what a "model" actually is |
| 1.3 | Kinds of learning: supervised, unsupervised, reinforcement |
| 1.4 | Train/test split and **overfitting** (memorising vs understanding) |
| 1.5 | Measuring a model: accuracy, precision, recall, and why accuracy can lie |
| 1.6 | How learning happens: error (loss) and small steps downhill (gradient descent), no heavy maths |
| 1.7 | Neural networks: layers of simple maths, explained with pictures |
| 1.8 | The only maths you need now: vectors, dot product, probability basics |

**Project P1:** a spam or sentiment classifier with scikit-learn on a public dataset. Report precision and
recall, and show one example of overfitting.

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Classifier | Logistic regression + gradient descent in `numpy` | `scikit-learn` (`LogisticRegression`, `train_test_split`, `classification_report`) | — |
| Neural network | Small network in `numpy` (forward and backward pass by hand) | **PyTorch** | — |
| Loading data | Download and parse the CSV yourself | Hugging Face `datasets` | — |

**Compare on:** the same test set → precision and recall (do your numbers match scikit-learn's? why or why not?) · training time · lines of code.

**Gate:** explain overfitting, precision vs recall, and what "training" changes inside a model.

### Stage 2 · How LLMs work `[BOTH]` · ~2–3 weeks
*Goal: know what's really happening when you send a prompt.*
| # | Lesson |
|---|--------|
| 2.1 | Tokens: how text becomes numbers |
| 2.2 | Next-token prediction: the one trick behind every LLM |
| 2.3 | Embeddings: meaning as a list of numbers (this connects to your old app!) |
| 2.4 | Transformers and attention: the intuition, no maths |
| 2.5 | How an LLM is made: pre-training → instruction tuning → human feedback (RLHF) |
| 2.6 | Temperature and sampling: why the same prompt gives different answers |
| 2.7 | The context window: the model's short-term memory |
| 2.8 | Why LLMs hallucinate (make things up) |
| 2.9 | The model landscape: closed vs open models, sizes, cost, reasoning models |

**Project P2:** `experiments/02_llm_lab/`: count tokens for different texts, run one prompt at 3 temperatures,
and build a small cost calculator.

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Tokens | Toy tokenizer in plain Python (split words, then a tiny BPE) | `tiktoken`, Hugging Face `tokenizers` | Your LLM provider's token-counting endpoint |
| Next-word prediction | Word-pair (bigram) model in plain Python | Small open model with Hugging Face `transformers` (`Qwen2.5-0.5B-Instruct` or `SmolLM2`) | Hosted LLM API (Claude) |
| **Embeddings** | Word-count / TF-IDF vectors by hand → a tiny word2vec in PyTorch | `sentence-transformers` with **`all-MiniLM-L6-v2`**, then `BAAI/bge-small-en-v1.5`, `intfloat/e5-small-v2`. Downloaded once, then runs on your CPU for free; **your text never leaves your machine.** | Embedding APIs: Voyage AI, OpenAI `text-embedding-3-small`. Pay per token, nothing to install, **your text is sent to the provider.** |

**Compare on:** the same 20 sentences → do the top-3 neighbours make sense? · speed · cost · vector size · privacy (does the text leave your machine?) · read each model's score on the MTEB leaderboard.

**Gate:** explain next-token prediction, context windows, and why hallucination happens, to a non-technical friend.

### Stage 3 · Using LLMs well: APIs and prompting `[BOTH]` · ~2–3 weeks
*Goal: get reliable, useful output from an LLM inside your code.*
| # | Lesson |
|---|--------|
| 3.1 | The messages API: system prompt, user and assistant roles, parameters |
| 3.2 | Streaming, errors, retries, and rate limits |
| 3.3 | Prompt engineering 1: clear instructions, context, examples (few-shot) |
| 3.4 | Prompt engineering 2: structure (XML tags), step-by-step thinking, prompt templates |
| 3.5 | Structured output: getting JSON you can trust (pydantic validation) |
| 3.6 | Tool calling basics: letting the model ask your code to do things |
| 3.7 | Testing prompts: from "looks good to me" to a small test set |
| 3.8 | Cost and speed: choosing the right model size for the job |

**Project P3:** a **structured extractor**: turn messy text (e.g. job posts) into validated JSON, with a
20-example test set and a pass rate.

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Retries | Your own retry loop with exponential backoff | `tenacity` (and the SDK's built-in retries) | — (the model is hosted in every version) |
| Structured output | Parse and validate JSON by hand | `pydantic` + `instructor` | The provider's built-in structured-output / tool-calling feature |
| Prompt tests | Your own loop over a test file, printing pass/fail | `promptfoo` (runs locally) | Hosted prompt/eval platforms (e.g. LangSmith, Braintrust) |

**Compare on:** pass rate on your 20 examples · invalid-JSON rate · code size · how clearly each one shows *why* a test failed.

**Gate:** improve a bad prompt live and explain each change; explain tool calling step by step.

### Stage 4 · Data skills `[BOTH]` · ~2 weeks
*Goal: AI is mostly data work. Get comfortable with it.*
| # | Lesson |
|---|--------|
| 4.1 | SQL basics: SELECT, WHERE, JOIN, GROUP BY |
| 4.2 | pandas for exploring and cleaning data |
| 4.3 | Text cleaning and parsing: HTML, Markdown, PDF |
| 4.4 | File formats: JSON, JSONL, CSV, Parquet |
| 4.5 | Data quality, licenses, and privacy: what you may and may not use |

**Project P4 (start of `docqa`):** fetch and clean the project corpus (GitLab handbook slice) with a
script, then explore it in pandas and SQLite.

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Reading data | `csv` / `json` from the standard library | `pandas` (or `polars`) | — |
| Database | Raw SQL with `sqlite3` | `SQLAlchemy` + Postgres running locally in Docker | Managed Postgres (e.g. Neon, Supabase, AWS RDS) |
| Parsing HTML/PDF | String and regex clean-up | `BeautifulSoup`, `pypdf` / `PyMuPDF` | Hosted document-parsing APIs (Stage 13) |

**Compare on:** time to do the same 3 analyses · row counts match? · how much text was lost or garbled in parsing.

**Gate:** write a JOIN + GROUP BY query from memory; explain why raw data stays out of git.

---

## BUILDING

### Stage 5 · Embeddings, search and RAG `[BOTH]` · ~5–6 weeks
*Goal: build question-answering over documents from scratch, and understand every piece.*
| # | Lesson |
|---|--------|
| 5.1 | Similarity search: embeddings + cosine similarity by hand (rebuild your old feature) |
| 5.2 | Where embedding search fails (exact IDs, negation, jargon) |
| 5.3 | What RAG is, and how it differs from similarity search |
| 5.4 | Chunking: splitting documents well |
| 5.5 | Building naive RAG step by step (no frameworks) |
| 5.6 | Keyword search (BM25) |
| 5.7 | Hybrid search and Reciprocal Rank Fusion |
| 5.8 | Vector databases and fast search (ANN / HNSW) |
| 5.9 | Reranking |
| 5.10 | Citations, grounding, and saying "I don't know" |
| 5.11 | Frameworks (LangChain / LlamaIndex): what they hide, and when to use them |

**Project:** `docqa` milestones **M1 → M3** (see `projects/README.md`).

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Chunking | Your own fixed-size + overlap splitter, then a by-heading splitter | LangChain `RecursiveCharacterTextSplitter`, LlamaIndex `SentenceSplitter` | — |
| Embeddings | Your TF-IDF vectors from Stage 2 | `sentence-transformers`: `all-MiniLM-L6-v2` vs `bge-small-en-v1.5` | Voyage AI / OpenAI embedding APIs |
| Vector search | `numpy` matrix + cosine, top-k by sorting | **Chroma** or **LanceDB** (embedded), **`pgvector`**, `FAISS` for very large sets | Managed vector DBs (e.g. Pinecone, Qdrant Cloud) |
| Keyword search | Your own BM25 | `rank_bm25`, Postgres full-text search | Managed search (e.g. Elasticsearch / OpenSearch services) |
| Hybrid | Your own Reciprocal Rank Fusion | Built-in hybrid search in vector DBs that have it (e.g. LanceDB, Qdrant, Weaviate) | Hybrid search in a managed vector DB |
| Reranking | Re-score the top 20 with your own LLM prompt | Cross-encoders: **`cross-encoder/ms-marco-MiniLM-L-6-v2`**, `BAAI/bge-reranker-base` | Rerank APIs (e.g. Cohere Rerank, Voyage rerank) |
| Whole RAG pipeline | Your own modules (`ingest` → `retrieve` → `generate`) | The **same pipeline rebuilt in LangChain and in LlamaIndex** (Lesson 5.11) | Managed "knowledge base" / file-search features from cloud or LLM providers (e.g. AWS Bedrock Knowledge Bases) |

**Compare on:** the same questions → recall@5 and answer quality · latency · cost per 1,000 questions · lines of code · how easy it was to find out *why* an answer was wrong · where the data lives.

**Gate:** draw the RAG pipeline from memory; explain RAG vs similarity search; explain why hybrid search beats either method alone.

### Stage 6 · Evaluation `[BOTH]` · ~2 weeks
*Goal: prove with numbers that your system works. Both roles are judged on this.*
| # | Lesson |
|---|--------|
| 6.1 | Why evals: "vibes" vs measurement |
| 6.2 | Building a golden test set |
| 6.3 | Retrieval metrics: recall@k, hit rate, MRR |
| 6.4 | Answer quality: faithfulness and correctness; LLM-as-judge and how to trust it |
| 6.5 | Eval-driven development: change one thing, re-measure |
| 6.6 | Writing an eval report a customer can read |

**Project:** `docqa` **M4**.

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Retrieval metrics | Your own recall@k, hit rate, MRR | `Ragas`, `DeepEval` | — |
| LLM judge | Your own rubric prompt | `Ragas` / `DeepEval` built-in judges | Hosted eval platforms (LangSmith, Braintrust, Langfuse) |
| Running and reporting | Your own `evals/run.py` → markdown table | `promptfoo` or `DeepEval`'s pytest integration | Dashboards on the same hosted platforms |

**Compare on:** the same golden set → do their scores match yours? Where they differ, check 5 items by hand: which one is right? · setup time · judge cost · can you see *why* a score was given?

**Gate:** explain recall@5 vs MRR; explain how you'd check that an LLM judge can be trusted.

### Stage 7 · Shipping software `[BOTH]` · ~2 weeks
*Goal: turn your script into a real service.*
| # | Lesson |
|---|--------|
| 7.1 | Building an API with FastAPI |
| 7.2 | Config, secrets, and logging (what never to log) |
| 7.3 | Testing with pytest |
| 7.4 | Docker: what a container is and why everyone uses them |
| 7.5 | CI with GitHub Actions |

**Project:** `docqa` **M5**.

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Web API | Python's built-in `http.server` | **FastAPI** + `uvicorn` | — |
| Tests | Plain `assert` scripts | `pytest` | — |
| Packaging | Run on your laptop with `venv` + a shell script | **Docker** image | — |
| CI | A local script you run before every push | — | **GitHub Actions** (hosted CI) |

**Compare on:** lines of code · input validation and `/docs` you got for free · "works on my machine" problems that Docker removed.

**Gate:** explain the request path from the user to the answer and back, including where logs are written.

> ### 🧭 ROLE CHECKPOINT
> Fill in `notes/role-checkpoint.md`:
> 1. Rate 1–5: building/tuning (Stages 5–6) vs shipping/operating (Stage 7) vs writing the eval report for a reader.
> 2. What did you lose track of time doing?
> 3. For one week, would you rather raise answer accuracy by 10%, or get the app running safely for a real customer?
> 4. Decide: **lean AIE**, **lean FDE**, or **balanced**. Re-check after Stage 12.

### Stage 8 · Knowledge graphs and GraphRAG `[BOTH]` concepts, `[AIE]` build depth · ~3 weeks
| # | Lesson |
|---|--------|
| 8.1 | Graphs 101: nodes and edges; similarity network vs knowledge graph |
| 8.2 | Triples, schemas, and ontologies |
| 8.3 | Extracting entities and relationships with an LLM |
| 8.4 | Entity resolution: "A. Chen" = "Alice Chen" |
| 8.5 | Graph databases and queries (NetworkX → Neo4j/Cypher) |
| 8.6 | GraphRAG: local vs global, and when it's worth the cost |

**Project:** `docqa` **M6** (GraphRAG measured against hybrid search).

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Graph storage | A Python dict of lists + your own breadth-first search | `NetworkX` (in memory), **Neo4j** in Docker (Cypher queries) | Managed graph DB (Neo4j AuraDB) |
| Entity extraction | Hand-written rules (regex + a list of known names) | `spaCy` named-entity model (`en_core_web_sm`) | LLM extraction with structured output (hosted API) |
| GraphRAG pipeline | Your own: find entities → walk the graph → prompt | Microsoft's `graphrag` package, LlamaIndex `PropertyGraphIndex` | — |

**Compare on:** 20 triples checked by hand → precision · the multi-hop question subset → accuracy · indexing cost (number of LLM calls) · build time.

**Gate:** explain when you would and wouldn't recommend GraphRAG to a customer.

### Stage 9 · Agents, tool use and MCP `[BOTH]`, deeper for `[AIE]` · ~3 weeks
| # | Lesson |
|---|--------|
| 9.1 | What an "agent" is: an LLM in a loop with tools |
| 9.2 | Writing the agent loop yourself (no framework) |
| 9.3 | Workflows vs agents: when NOT to use an agent |
| 9.4 | Guardrails for agents: step limits, timeouts, permissions, human approval |
| 9.5 | MCP (Model Context Protocol): connecting tools and data to any AI app |
| 9.6 | Multi-agent systems: when they help, when they're hype |
| 9.7 | Evaluating agents |

**Project:** `docqa` **M7**: agent mode + an MCP server that exposes your search as a tool.

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Agent loop | Your own `while` loop handling tool calls | **LangGraph**, **Claude Agent SDK** | Managed agent services from LLM providers |
| Tools via MCP | A tiny tool server you write yourself | Official **MCP Python SDK** | Remote (hosted) MCP servers |

**Compare on:** the same 10 tasks → success rate · steps · cost · how readable the traces are · how hard it is to add a guardrail (e.g. a step limit).

**Gate:** explain the agent loop step by step; explain what MCP solves.

### Stage 10 · Customizing models `[AIE]` deep, `[FDE]` light · ~2–3 weeks
| # | Lesson |
|---|--------|
| 10.1 | Prompting vs RAG vs fine-tuning: which fixes which problem |
| 10.2 | Open-source models and running them locally (Ollama) |
| 10.3 | Fine-tuning and LoRA, in simple terms |
| 10.4 | Quantization: making models smaller and faster |
| 10.5 | Serving models (vLLM idea, GPUs, throughput vs latency) |
| 10.6 | Distillation and small models for cheap tasks |

**Project P5:** compare a local open model with your API model on your eval set. `[AIE]`: also run a small
LoRA fine-tune (free Colab GPU).

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Training | A tiny PyTorch training loop | Hugging Face `transformers` + `peft` (LoRA) on `Qwen2.5-0.5B` or `SmolLM2` (free Colab GPU) | Hosted fine-tuning APIs from LLM / cloud providers |
| Running a model | Load weights and generate with plain `transformers` code | **Ollama**, `llama.cpp` with quantized GGUF models (Llama, Qwen, Mistral, Gemma) | The hosted LLM API you've used so far |
| Serving | Your FastAPI app wrapping a model | `vLLM` | Managed model hosting (AWS Bedrock, Google Vertex AI, Azure AI Foundry) |

**Compare on:** your eval set → quality · tokens per second · cost per 1,000 questions · hardware needed · privacy (could a customer run it inside their own network?).

**Gate:** a customer asks "should we fine-tune?" Give a clear decision process.

---

## PRODUCTION + CUSTOMER

### Stage 11 · LLMOps, security and safety `[BOTH]` · ~3 weeks
| # | Lesson |
|---|--------|
| 11.1 | Cost and latency: measuring p50/p95, caching, prompt caching |
| 11.2 | Observability: logs, traces, dashboards |
| 11.3 | Versioning prompts, models, and datasets; regression testing |
| 11.4 | Prompt injection (direct and indirect) and data leaks |
| 11.5 | Guardrails: input/output checks, PII redaction |
| 11.6 | Responsible AI: bias, transparency, human oversight |
| 11.7 | Compliance basics in plain words: GDPR, SOC 2, data residency, retention |

**Project:** `docqa` hardening: caching, tracing, a threat model, a 10-item attack test set.

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Logging and tracing | Request-ID logs + your own timers | OpenTelemetry; **Langfuse** self-hosted in Docker | Langfuse Cloud, LangSmith |
| Caching | A Python dict | **Redis** in Docker | Managed Redis + the LLM provider's prompt caching |
| PII masking | Your own regex | Microsoft **Presidio** | Cloud PII-detection services (e.g. AWS Comprehend, Google Cloud DLP) |
| Guardrails | Your own input/output checks | Guardrail libraries (e.g. NeMo Guardrails, Guardrails AI) | Hosted moderation / guardrail APIs |

**Compare on:** your 10-item attack set → what each version catches · latency added · cost · where sensitive data goes.

**Gate:** explain indirect prompt injection with an example, plus 2 defences and their limits.

### Stage 12 · Cloud, networking, auth and integration `[BOTH]` basics, `[FDE]` deep · ~3–4 weeks
| # | Lesson |
|---|--------|
| 12.1 | Networking basics: IP, DNS, ports, HTTP vs HTTPS/TLS |
| 12.2 | Inside a company network: firewalls, proxies, VPCs, private endpoints |
| 12.3 | Cloud basics (one cloud, e.g. AWS): compute, storage, IAM, managed AI services |
| 12.4 | AuthN vs AuthZ; sessions vs tokens (JWT); this time you'll truly understand your old login app |
| 12.5 | OAuth2, OIDC and SSO: how a customer's Okta/Entra login works |
| 12.6 | Permission-aware retrieval: users must only see their own documents |
| 12.7 | Integrations: REST APIs, webhooks, connectors (Google Drive, SharePoint, Slack) |
| 12.8 | Deploying and operating: secrets, monitoring, runbooks, rollbacks |

**Project:** `docqa` **M8**: auth + permission filtering + leak tests + cloud deployment + `RUNBOOK.md`.

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| Login | Session login + password hashing by hand (*learning only*: never hand-roll security in real work) | **Keycloak** (self-hosted identity provider) + `Authlib` | Hosted identity providers (**Auth0**, Okta, Entra ID) |
| Tokens | Decode a JWT by hand (base64) and check its fields | `PyJWT` / `Authlib` | — |
| Permission filtering | Your own ACL filter applied *before* search | Vector DB metadata filters | — |
| Cloud resources | Click through the cloud console once | `boto3` scripts, **Terraform** `[FDE]` | — |
| **Deployment** | By hand: SSH into a small VM, install Python, run `uvicorn` under `systemd` | Docker Compose on that VM; Terraform to create it | Managed platforms (Render / Fly.io / Railway, AWS App Runner, Google Cloud Run) |

**Compare on:** steps to redeploy · time to recover after a crash · how secrets are stored · monthly cost · which option you'd offer a customer whose data must stay inside their network.

**Gate:** draw the SSO login flow; explain why permission filtering must happen *before* search results reach the LLM.

**Re-check your role lean here.**

### Stage 13 · Multimodal AI `[BOTH]` light, `[AIE]` deeper · ~1–2 weeks
| # | Lesson |
|---|--------|
| 13.1 | Vision: LLMs that read images, screenshots, and scanned documents |
| 13.2 | Document AI: PDFs with tables and forms |
| 13.3 | Speech: speech-to-text and text-to-speech |

**Project:** add PDF/image ingestion to `docqa`, and measure how it does on documents with tables.

**🧰 Scratch → package**

| Piece | ① From scratch (your own code) | ② Local package / pretrained model (runs on your machine) | ③ Hosted API / managed service (runs on a provider's servers) |
|---|---|---|---|
| PDFs with tables | `pypdf` plain text + your own table heuristics | `docling`, `PyMuPDF` | Vision LLM reading page images; document-AI services (AWS Textract, Azure Document Intelligence) |
| Speech-to-text | — | `faster-whisper` (Whisper running on your machine) | Hosted speech-to-text APIs |

**Compare on:** 10 documents with tables → cell accuracy · speed · cost per page · privacy.

**Gate:** explain when to use a vision model vs plain text extraction.

### Stage 14 · FDE craft: working with customers `[FDE]` core, `[BOTH]` useful · ~3 weeks
| # | Lesson |
|---|--------|
| 14.1 | Discovery: asking good questions; finding the real problem |
| 14.2 | Scoping: success criteria, what's in and what's out |
| 14.3 | Writing: design docs, status updates, decision memos |
| 14.4 | Demos that build trust |
| 14.5 | Communicating limits honestly ("will it hallucinate?") |
| 14.6 | Handling escalations and bad news |
| 14.7 | Security reviews and questionnaires |
| 14.8 | Feeding customer needs back to the product team |

**Project P6:** customer simulation ("Acme Corp"): scoping doc, security answers, limitations memo,
results on their data, and a recorded 10-minute demo.

**🧰 Scratch → package**

*No code in this stage, so the rule becomes: write your own version first, then compare it with a real-world template.*

| Piece | ① Your own version first (blank page) | ② Real-world template / reference |
|---|---|---|
| Discovery and scoping | Your own question list and scope doc | A public statement-of-work / scoping template |
| Security questionnaire | Your own answers | Standard questionnaire formats: CSA **CAIQ**, **SIG Lite** |
| Design doc / memo | Your own structure | A well-known public design-doc template |

**Compare on:** what the template made you think about that you missed · what you'd keep from your own version.

**Gate:** role-play: the customer says "it's giving wrong answers." Walk through your first hour.

---

## FINISH

### Stage 15 · System design for AI `[BOTH]` · ~2 weeks
| # | Lesson |
|---|--------|
| 15.1 | How to approach a system design question |
| 15.2 | Design: company-wide RAG for 10k employees with SSO and permissions |
| 15.3 | Design: a customer-support agent with human hand-off |
| 15.4 | Design: a document-processing pipeline at scale |
| 15.5 | Trade-offs: cost vs quality vs latency vs safety |

**🧰 Scratch → package**

*No code in this stage, so the rule becomes: write your own version first, then compare it with a real-world template.*

| Piece | ① Your own version first (blank page) | ② Real-world template / reference |
|---|---|---|
| System design | Your own design on paper | Published reference architectures for RAG / agents from AWS, Azure, and Google Cloud |

**Compare on:** components you missed · trade-offs you made differently, and whose choice fits the scenario better (and why).

**Gate:** one full written design, reviewed by Claude.

### Stage 16 · Specialize, portfolio, interviews `[BOTH]` · ~3–4 weeks
- Deep dive into your lean (`[AIE]` model/eval depth, or `[FDE]` multi-tenant, VPC, customer-handoff depth).
- Clean up the repo: README with **numbers**, architecture, trade-offs.
- A write-up: "From naive RAG to GraphRAG and agents, with measurements."
- 5 STAR stories from this repo, mock interviews, the final cumulative quiz.

**🧰 Scratch → package**

*No code in this stage, so the rule becomes: write your own version first, then compare it with a real-world template.*

| Piece | ① Your own version first (blank page) | ② Real-world template / reference |
|---|---|---|
| Portfolio README | Your own | READMEs of well-known open-source AI projects |
| Interview answers | Your own answers | Real questions collected in `notes/job-market.md` |

**Compare on:** can a stranger understand it in 2 minutes? · which real questions you couldn't answer yet.

---

## ONGOING TRACK · Staying current (jobs + tech) `[BOTH]`
AI changes every month. This track runs **alongside** the stages from week 1, in small fixed amounts, so
you stay up to date without it eating your learning time.

| When | Time | What | Where it's logged |
|------|------|------|-------------------|
| Every Sunday | 20 min | **Tech radar:** skim 2–3 sources from the list below. Write down 1–3 things that are new, each in one sentence: what it is, and which stage it relates to. | `notes/tech-radar.md` |
| Once a month (1st Sunday) | 30 min | **Job scan:** read 5 real job posts (AI Engineer + FDE). Tally the skills they ask for. | `notes/job-market.md` |
| Every 3 months | 30 min | **Plan update:** Claude compares your job-market tally with this plan and suggests adding, moving, or dropping lessons. Nothing changes without your OK. | This file |

**Rules (so it doesn't turn into procrastination):**
- Never instead of the lesson; always after it, or on Sunday.
- Hard cap: 20 min/week for news. Bookmark the rest and let it go.
- A new tool goes on the radar, **not** into the plan, until it appears in job posts or keeps coming up for 2+ months.

**Starter sources:**
- **Model makers:** official blogs, changelogs, and docs of Anthropic, OpenAI, and Google DeepMind
- **Practitioners:** Simon Willison's blog · Latent Space (newsletter and podcast) · Chip Huyen (blog and the book *AI Engineering*) · Hamel Husain and Eugene Yan (evals and applied ML) · The Batch (DeepLearning.AI)
- **Discussion:** Hacker News front page (skim titles only)
- **Jobs:** "AI Engineer", "Applied AI Engineer", and "Forward Deployed Engineer" postings on LinkedIn and on AI company career pages

**About "learning everything":** nobody knows everything in AI, and new tools appear every week. The
stages above are the **core that stays useful**: how models work, building, evaluating, shipping,
securing, and working with customers. This track keeps the rest up to date. A new tool is easy to
pick up once you know the core.

---

## Progress
| Stage | Status | Passed on |
|-------|--------|-----------|
| 0 The big map | 🔵 in progress | — |
| 1 How ML learns | ⬜ | — |
| 2 How LLMs work | ⬜ | — |
| 3 Using LLMs well | ⬜ | — |
| 4 Data skills | ⬜ | — |
| 5 Search and RAG | ⬜ | — |
| 6 Evaluation | ⬜ | — |
| 7 Shipping software | ⬜ | — |
| 8 Knowledge graphs | ⬜ | — |
| 9 Agents and MCP | ⬜ | — |
| 10 Customizing models | ⬜ | — |
| 11 LLMOps and safety | ⬜ | — |
| 12 Cloud, network, auth | ⬜ | — |
| 13 Multimodal | ⬜ | — |
| 14 FDE craft | ⬜ | — |
| 15 System design | ⬜ | — |
| 16 Portfolio and interviews | ⬜ | — |

**Current lesson:** 0.1 · see [`lessons/`](lessons/)
