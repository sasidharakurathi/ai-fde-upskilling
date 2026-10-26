# Practice Projects

Everything here is **built by you, from scratch**. Claude gives hints, reviews, and explanations. It
doesn't write the project code unless you explicitly ask, because typing it yourself is how it sticks.

```
projects/
  docqa/            # the one app that grows through milestones M1–M8
  customer-sim/     # Week 14 scoping, security answers, limitations memo
experiments/        # small throwaway scripts (Week 1 embeddings, etc.)
```

## The corpus (decide in Week 1, Saturday)

Requirements: public, a license that allows learning use, **enterprise-like** (so the FDE exercises are
realistic), full of **entities and relationships** (for the knowledge graph), splittable into
**departments** (for permission tests in Week 12), and 100–300 pages.

**Recommended:** a slice of **GitLab's public company handbook** (handbook.gitlab.com). It's real
company documentation: teams, roles, policies, processes, tools. Pick 3–4 sections (e.g. engineering,
security, people/HR, support). Each section later becomes a permission group.
**Alternative:** ~100 Wikipedia articles on one domain you like.

Rules:
- Check and note the license in `projects/docqa/DATA.md`.
- **Don't commit raw data.** Commit `scripts/fetch_data.py`; `data/` goes in `.gitignore`.
- Finding the handbook's source files and downloading them is part of the task.

## Milestones and acceptance criteria

| # | Week | Milestone | Done when |
|---|------|-----------|-----------|
| M1 | 2 | **Naive RAG from scratch** | `docqa ask "q"` returns an answer from top-k chunks; modules split; chunker tests pass; README has an architecture diagram; `FAILURES.md` labels 10 questions. |
| M2 | 3 | **Retrieval modes** | `--mode semantic\|bm25\|hybrid\|hybrid_rerank`; RRF written by you; vector store in use; comparison table. |
| M3 | 4 | **Citations and grounding** | Structured `{answer, citations}`; citation checker; declines unanswerable questions; minimal UI with sources. |
| M4 | 5 | **Evaluation** | 40–50-question golden set; recall@k / MRR / hit rate; LLM judge with measured agreement; `evals/run.py`; `EVAL_REPORT.md`. |
| M5 | 6 | **Served** | FastAPI `/ask` + `/health`; structured logs; Docker; CI green. |
| M6 | 8 | **GraphRAG experiment** | Ontology; extracted KG; graph-augmented retrieval; baseline vs graph on a multi-hop subset; `GRAPHRAG_REPORT.md` with cost. |
| M7 | 10–11 | **Agent + production hardening** | Hand-written tool loop with traces + agent eval; caching/retries; threat model; adversarial eval set. |
| M8 | 12–13 | **Secure deployment** | Auth + groups; ACL filtering before ranking; leak tests (incl. cache); deployed with HTTPS; `RUNBOOK.md` tested from a clean clone. |
| — | 14 | **Customer simulation** | `customer-sim/` scoping, security answers, limitations memo, results report, recorded demo. |

## Definition of "done" for any task
1. It runs from a clean checkout with the documented command.
2. It's committed with a clear message.
3. You can explain *why* it works (or why it doesn't) in two sentences.
