# Practice Projects

Everything here is **built by you, from scratch**. Claude gives hints, reviews, and explanations. It
doesn't write the project code unless you explicitly ask, because typing it yourself is how it sticks.

```
experiments/        # small learning scripts (P0, P2, ...)
projects/
  classifier/       # P1 · Stage 1
  extractor/        # P3 · Stage 3
  docqa/            # P4 · the main app, grows from Stage 4 to Stage 13 (milestones M1–M8)
  local-models/     # P5 · Stage 10
  customer-sim/     # P6 · Stage 14
```

## Projects by stage

| Project | Stage | What you build | Done when |
|---------|-------|----------------|-----------|
| **P0** hello LLM | 0 | `experiments/00_hello_llm.py`: one API call | Prints answer, token counts, cost; the API key is not in git. |
| **P1** classifier | 1 | Spam/sentiment classifier: first in plain `numpy`, then with scikit-learn, on a public dataset | Reports precision + recall on a test set; shows one example of overfitting and explains it. |
| **P2** LLM lab | 2 | `experiments/02_llm_lab/`: tokens, temperature, cost, embeddings by hand vs `all-MiniLM-L6-v2` | Token counts for 5 texts; one prompt at 3 temperatures compared; cost calculator works. |
| **P3** extractor | 3 | Messy text → validated JSON (pydantic) | 20-example test set with a pass rate; a prompt change that measurably improved it. |
| **P4** `docqa` | 4–13 | Question answering over a document collection | See the milestones below. |
| **P5** local models | 10 | Local open model vs API model on your eval set | Comparison table (quality, speed, cost). `[AIE]`: plus a small LoRA fine-tune. |
| **P6** customer sim | 14 | "Acme Corp" engagement | Scoping doc, security answers, limitations memo, results report, recorded demo. |

## `docqa` corpus (chosen in Stage 4)
Requirements: public, a license that allows learning use, **company-like** (so the FDE exercises are
realistic), full of **entities and relationships** (for the knowledge graph), and splittable into
**departments** (for permission tests).

**Recommended:** a slice of **GitLab's public company handbook** (handbook.gitlab.com). Pick 3–4 sections
(e.g. engineering, security, people/HR, support). **Alternative:** ~100 Wikipedia articles on one domain.

Rules: check and note the license in `projects/docqa/DATA.md`; **don't commit raw data** (commit
`scripts/fetch_data.py`; `data/` goes in `.gitignore`).

## `docqa` milestones

| # | Stage | Milestone | Done when |
|---|-------|-----------|-----------|
| M0 | 4 | **Data ready** | One command fetches and cleans the corpus; explored in pandas/SQLite. |
| M1 | 5 | **Naive RAG from scratch** | `docqa ask "q"` answers from top-k chunks; code split into modules; chunker tests; architecture diagram; `FAILURES.md` with 10 labelled questions. |
| M2 | 5 | **Retrieval modes** | `--mode semantic\|bm25\|hybrid\|hybrid_rerank`; RRF written by you; vector DB in use; comparison table. |
| M3 | 5 | **Citations and grounding** | `{answer, citations}` output; citation checker; declines unanswerable questions; minimal UI with sources. |
| M4 | 6 | **Evaluation** | 40–50-question golden set; recall@k / MRR; LLM judge with measured agreement; `evals/run.py`; `EVAL_REPORT.md`. |
| M5 | 7 | **Served** | FastAPI `/ask` + `/health`; structured logs; Docker; CI green. |
| M6 | 8 | **GraphRAG experiment** | Ontology; extracted knowledge graph; graph-augmented retrieval; measured vs hybrid on multi-hop questions; `GRAPHRAG_REPORT.md` with cost. |
| M7 | 9 | **Agent + MCP** | Hand-written agent loop with traces; agent eval; MCP server exposing search. |
| M8 | 11–13 | **Production-ready** | Caching and tracing; threat model and attack tests; auth + permission filtering + leak tests; deployed with HTTPS; `RUNBOOK.md`; PDF/image ingestion. |

## Scratch → package rule
Every project is built in up to three versions, following its stage's 🧰 table in `LEARNING_PLAN.md`:
**① from scratch** (plain Python + `numpy`) → **② local package / pretrained model**, which runs on your machine
(e.g. `sentence-transformers` + `all-MiniLM-L6-v2`, Chroma) → **③ hosted API / managed service**, which runs on
a provider's servers (e.g. an embedding API, a managed vector DB). Each project keeps a `NOTES.md` with a
**Compare** section, run on the same test inputs: results, speed and cost, code, what the package hid, where
the data goes, and which version you'd use at work.

## Definition of "done" for any task
1. It runs from a clean checkout with the documented command. Every version in the stage's 🧰 table works.
2. It's committed with a clear message.
3. You can explain *why* it works (or why it doesn't) in two sentences.
