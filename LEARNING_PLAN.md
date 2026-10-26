# Learning Plan: AI Engineer / Forward Deployed Engineer

**Start:** Mon 2026-10-26 · **Length:** 16 weeks (incl. 1 holiday buffer) · **Role checkpoint:** end of Week 6

## How this plan works

**Your time budget**
| Day       | Time       | What happens                                                        |
|-----------|------------|---------------------------------------------------------------------|
| Mon–Fri   | ~1 hour    | One small task with a clear "done when". Friday includes a quiz.    |
| Saturday  | 3–4 hours  | **Build block**: finish the week's project milestone.               |
| Sunday    | ~45 min    | Weekly review + quiz. Optional 1–2 h catch-up/stretch (never mandatory). |

**Tags**
- `[BOTH]`: core for both roles. Never skip these.
- `[AIE]`: AI Engineer depth (retrieval quality, evals, agents, models).
- `[FDE]`: Forward Deployed depth (deployment, auth, integration, security, customer communication).
- *Stretch* tasks go in Sunday catch-up time and are optional. After Week 6, do the stretch tasks for
  your chosen lean.

**Rules**
1. **The plan is ordered by task, not by date.** Dates are targets. If you fall behind, the plan
   *slides*. Never do two days of work in one day to "catch up" (see `tracking/CONSISTENCY.md`).
2. **Build from scratch first, frameworks later.** You'll write chunking, retrieval, RRF, and eval
   metrics yourself before touching LangChain/LlamaIndex, so you know what those tools hide.
3. **Every task ends with a commit** and a check-in line in `tracking/CHECKINS.md`.
4. **"Done when"** is the finish line. Hitting it in 40 minutes means you're done for the day. Not
   hitting it in 75 minutes means you write down where you got stuck and stop. Tomorrow you start
   from that note.

**Projects:** one app, `projects/docqa/`, grows through milestones M1–M8 (spec in
[`projects/README.md`](projects/README.md)). Small throwaway exercises go in `experiments/`.

**Stack (small budget):** Python 3.12, `uv`, local embeddings (`sentence-transformers`, free), one paid
LLM API for generation (budget alert at $10/month), SQLite/numpy → Chroma or LanceDB, FastAPI,
Docker, pytest, GitHub Actions.

---

## Phase 1 — Shared foundation (Weeks 1–6) · all `[BOTH]`

### Week 1 · Oct 26 – Nov 1 · Concepts + embeddings from scratch `[BOTH]`
| Day | Task | Done when |
|-----|------|-----------|
| Mon | Read `notes/concepts.md` §1–2. Write your RAG-vs-similarity explanation in `notes/my-words.md` **without looking**. | Committed; 5 sentences max. |
| Tue | Set up the env: `uv`, `.gitignore`, `.env` (API key, **gitignored**), `ruff`. Write `experiments/01_hello_llm.py`: one prompt, print the reply + input/output token counts. Set a billing alert. | Script prints token usage; `git status` shows no `.env`. |
| Wed | `experiments/02_embeddings.py`: embed 20 sentences locally, compute cosine similarity **by hand with numpy** (dot product / norms), print the top-3 for a query. | You can say why a dot product of normalized vectors = cosine. |
| Thu | **Rebuild your old feature:** "find similar items" over ~50 short texts. Find 3 queries where it fails (an exact ID, negation, jargon). | Failures + your guess at *why* written in the script's docstring. |
| Fri | Tokens, context windows, temperature, pricing. Calculate: cost of sending a 10-page document 1,000 times with your model. **Quiz #1** (concepts §1–2). | Cost calc in `notes/my-words.md`; quiz logged. |
| Sat | Read concepts §3–5. **Pick and fetch the corpus** (see `projects/README.md`). Write `projects/docqa/scripts/fetch_data.py` → `data/raw/` (gitignored). Count docs, words, rough tokens. | One command rebuilds the dataset from nothing. |
| Sun | Weekly review #1. Fill in `notes/my-words.md` for §3–5. | Review written; streak updated. |

### Week 2 · Nov 2 – 8 · M1: Naive RAG from scratch `[BOTH]`
| Day | Task | Done when |
|-----|------|-----------|
| Mon | Chunker: fixed size with overlap; keep metadata (doc id, title, section, position). Look at 10 chunks by eye. | You've noted 2 places where a split cuts meaning. |
| Tue | Embed all chunks; save vectors (`.npy`) + metadata (JSON or SQLite). Measure time and file size. | Index builds with one command. |
| Wed | `search(query, k)` → chunks + scores. Try 10 real questions. | Each of the 10 marked "right chunk in top-5: yes/no". |
| Thu | Generation: a prompt that answers **only** from the given chunks. CLI: `docqa ask "..."`. | End-to-end answer printed. |
| Fri | **Failure log**: for the 10 questions, label each as *retrieval miss* or *generation error* or *OK*. **Quiz #2**. | `projects/docqa/FAILURES.md` exists. |
| Sat | Split into modules (`ingest`, `index`, `retrieve`, `generate`, `cli`); pytest for the chunker; README with an ASCII architecture diagram. | **M1 done** (criteria in projects/README.md). |
| Sun | Weekly review #2. *Stretch:* read one "RAG from scratch" article and compare it with your design. | — |

### Week 3 · Nov 9 – 15 · M2: Keyword, semantic, hybrid, rerank `[BOTH]` (AIE depth)
| Day | Task | Done when |
|-----|------|-----------|
| Mon | Learn BM25 (term frequency, inverse document frequency, length normalization). Add BM25 retrieval (`rank_bm25`). Re-run the failure-log questions. | Note which questions BM25 fixes and which it breaks. |
| Tue | **Implement Reciprocal Rank Fusion yourself** (~15 lines) to combine BM25 + vector rankings. | You can explain why we fuse *ranks*, not *scores*. |
| Wed | Chunking experiment: split by heading/paragraph vs fixed size. Compare on your questions. | 1-paragraph result in `FAILURES.md`. |
| Thu | Move vectors to a vector store (Chroma or LanceDB). Learn what ANN/HNSW does at a high level; use a metadata filter. | Same results as numpy on 5 queries. |
| Fri | Reranking: retrieve top-20 → cross-encoder → top-5. **Quiz #3**. | Rerank toggle works. |
| Sat | Config flag `--mode semantic|bm25|hybrid|hybrid_rerank`; comparison table over your questions. | **M2 done**. |
| Sun | Weekly review #3. | — |

### Week 4 · Nov 16 – 22 · M3: Citations, grounding, "I don't know" `[BOTH]`
| Day | Task | Done when |
|-----|------|-----------|
| Mon | Stable chunk IDs; structured output `{answer, citations:[chunk_id]}`; cite after each claim. | JSON validates with pydantic. |
| Tue | Citation checker: every cited ID must be in the context given to the model; flag sentences with no citation. | Checker catches a hand-made bad answer. |
| Wed | Write 5 questions the corpus **cannot** answer. Make the system decline (prompt + retrieval score threshold). | 5/5 correctly declined, or the failures are written down. |
| Thu | Show sources: title, link/path, quoted snippet for each citation. | Output is checkable by a human in < 30 s. |
| Fri | **Prompt-injection demo:** plant "ignore previous instructions…" in a document and see what happens. Try one mitigation. **Quiz #4**. | Before/after written in `notes/security.md`. |
| Sat | Minimal UI (Streamlit, or FastAPI + one HTML page) showing the answer + citations. | **M3 done**. |
| Sun | Weekly review #4. | — |

### Week 5 · Nov 23 – 29 · M4: Evaluation `[BOTH]` (the skill both roles are judged on)
| Day | Task | Done when |
|-----|------|-----------|
| Mon | Golden set v1: 30 rows `{question, expected_answer, relevant_chunk_ids, type}`. Types: lookup, multi-part, no-answer, exact-term, multi-hop. | `evals/golden.jsonl` committed. |
| Tue | Implement **recall@k, hit rate, MRR** by hand. Run for every retrieval mode. | Table of numbers per mode. |
| Wed | Generation eval: an LLM judge with a rubric (faithful? correct? cited?). Label 10 yourself and measure judge agreement. | Agreement % recorded; you trust (or don't) the judge, with a reason. |
| Thu | `evals/run.py`: one command → dated markdown results file with config + cost + latency. | Re-runs are reproducible. |
| Fri | Analyse: best config, by question type. Cost and p50 latency per query. **Quiz #5**. | 5 bullet findings. |
| Sat | Grow the set to 40–50 questions. Write `EVAL_REPORT.md` **as if for a customer**: what works, what fails, recommendation. | **M4 done**. |
| Sun | Weekly review #5. | — |

### Week 6 · Nov 30 – Dec 6 · M5: Serve it + ROLE CHECKPOINT `[BOTH]`
| Day | Task | Done when |
|-----|------|-----------|
| Mon | FastAPI: `POST /ask`, `GET /health`; pydantic request/response; config from env vars. | curl returns an answer. |
| Tue | Structured logging: request id, retrieved ids, latency, tokens, cost. **Never log secrets.** | One JSON log line per request. |
| Wed | Dockerfile + `.dockerignore`; ingestion as a separate command. | `docker run` serves `/ask`. |
| Thu | API tests (pytest + TestClient); GitHub Actions running ruff + tests. | Green CI badge. |
| Fri | **Quiz #6 (cumulative, mock-interview style):** explain the whole system in 5 minutes. | Logged. |
| Sat | **Role checkpoint:** fill in `notes/role-checkpoint.md` (template below). README polish. | **M5 done** + lean chosen. |
| Sun | Weekly review #6. | — |

**Role checkpoint template** (`notes/role-checkpoint.md`):
1. Rate 1–5 how much you enjoyed: W3 retrieval tuning · W5 evals · W6 API/Docker/CI · writing EVAL_REPORT.
2. What did you do *voluntarily* or lose track of time on?
3. Which would you rather do for a week: improve recall@5 by 10 points, or get the app running securely for a real customer?
4. Decision: **lean AIE**, **lean FDE**, or **stay balanced**. Re-check at Week 12.

---

## Phase 2 — Going deeper (Weeks 7–11)

### Week 7 · Dec 7 – 13 · Knowledge graphs `[BOTH]` concepts, `[AIE]` depth
| Day | Task | Done when |
|-----|------|-----------|
| Mon | Re-read concepts §3. Design an **ontology** for your corpus: 4–6 entity types, 5–8 directed relationship types. | `graph/ontology.md` with an example triple per relation. |
| Tue | Hand-build 20–30 triples from 3 documents in NetworkX. Query neighbours and paths. | 2 multi-hop queries answered by graph traversal. |
| Wed | LLM extraction: JSON-schema-constrained triples per chunk, restricted to your ontology. Run on 10 chunks. | Output validates. |
| Thu | Compare LLM triples vs your hand-built ones. Handle **entity resolution** (name normalization). | Rough precision/recall written down. |
| Fri | Build a **similarity network** of docs too; list 3 questions each can answer that the other can't. **Quiz #7**. | Written in `notes/my-words.md`. |
| Sat | **Estimate the cost first**, then extract over the full corpus; save the graph (GraphML); visualize a subgraph. *Stretch [AIE]:* load into Neo4j and write 3 Cypher queries. | Graph file + picture committed. |
| Sun | Weekly review #7. | — |

### Week 8 · Dec 14 – 20 · M6: GraphRAG experiment `[BOTH]` eval, `[AIE]` build depth
| Day | Task | Done when |
|-----|------|-----------|
| Mon | Add 10 **multi-hop/relationship** questions to the golden set. Run the hybrid baseline on them. | Baseline numbers for the multi-hop subset. |
| Tue | Graph retrieval: entity linking (query → KG nodes) → 1–2 hop subgraph → triples + their source chunks. | Returns facts with chunk ids. |
| Wed | Combine graph facts + hybrid chunks in the prompt; every fact still cites a chunk. | End-to-end answer. |
| Thu | Eval: baseline vs graph-augmented, overall **and** multi-hop subset. Include indexing cost. | Table in results. |
| Fri | Read the Microsoft GraphRAG paper (community detection + summaries, global vs local search). Write: "When would I recommend GraphRAG to a customer?" **Quiz #8**. | Half-page answer. |
| Sat | `GRAPHRAG_REPORT.md`: did it help, on what, at what cost. *Stretch [AIE]:* community summaries for 3 "global" questions. *Stretch [FDE]:* a 1-page recommendation memo for a fictional customer incl. maintenance burden. | **M6 done**. |
| Sun | Weekly review #8. | — |

### Week 9 · Dec 21 – 27 · HOLIDAY BUFFER
No new material. Finish any unfinished milestone. If everything is done: do the bad-day minimum (see
`tracking/CONSISTENCY.md`) on most days, plus one review quiz. Rest is allowed and planned; it
doesn't break the streak if declared in the Week 8 review.

### Week 10 · Dec 28 – Jan 3 · Agents and tool use `[BOTH]`, `[AIE]` depth
| Day | Task | Done when |
|-----|------|-----------|
| Mon | Tool calling with the raw API: one tool `search_docs`; write the agent loop yourself (no framework). | Model calls the tool and answers. |
| Tue | Add tools: `get_document(id)`, `graph_neighbors(entity)`. | Model picks the right tool in 3 test prompts. |
| Wed | Guardrails: max steps, timeouts, tool errors, a trace log of every step. | A broken tool doesn't crash the loop. |
| Thu | Agent eval: 10 tasks → success rate, steps, cost. Compare with plain RAG. | Honest verdict: is the agent worth it? |
| Fri | Read Anthropic's "Building effective agents" (workflows vs agents). **Quiz #9**. | 3 takeaways in your words. |
| Sat | `/ask?mode=agent` with traces returned; write "when NOT to use an agent". | **M7a done**. |
| Sun | Weekly review #9. | — |

### Week 11 · Jan 4 – 10 · Production concerns `[BOTH]`
| Day | Task | Done when |
|-----|------|-----------|
| Mon | Measure p50/p95 latency and tokens/query; try prompt caching and a smaller model for cheap steps. | Before/after numbers. |
| Tue | Caching (embeddings, answers) + retries with exponential backoff + rate-limit handling. | Repeated query is ~free. |
| Wed | Tracing with request ids across retrieve → generate (optional: Langfuse or OpenTelemetry). | One request fully traceable. |
| Thu | Threat model 1-pager: indirect prompt injection, data exfiltration, PII in logs, over-permissioned tools. | `notes/security.md` updated. |
| Fri | **Quiz #10**. | — |
| Sat | Implement 2 mitigations + a 10-item adversarial eval set. | **M7b done**. |
| Sun | Weekly review #10. | — |

---

## Phase 3 — Deployment exercise (Weeks 12–14) · `[BOTH]` with `[FDE]` depth

### Week 12 · Jan 11 – 17 · Auth and permission-aware retrieval `[BOTH]`, `[FDE]` depth
*This ties back to the login/access-control app you built before. This time you'll be able to explain it.*
| Day | Task | Done when |
|-----|------|-----------|
| Mon | AuthN vs AuthZ; sessions vs JWT; draw the OAuth2/OIDC login flow on paper; what SSO means for a customer (their IdP: Okta, Entra ID…). | Diagram photo/ASCII in `notes/auth.md`. |
| Tue | Add auth to the API (API keys or JWT) with users and groups. | Unauthenticated `/ask` → 401. |
| Wed | Document ACLs: each doc has allowed groups; **filter before ranking**, never after. Write down why post-filtering leaks. | Retrieval respects groups. |
| Thu | Leak tests: user A can't get a restricted doc via `/ask`, citations, the agent tools, **or the cache** (the cache key must include the permission scope). | 4 tests green. |
| Fri | **Quiz #11**. Re-check your role lean. | — |
| Sat | *Stretch [FDE]:* real OIDC login via Keycloak or a free Auth0 tenant. *Stretch [AIE]:* run evals per user role. | **M8a done**. |
| Sun | Weekly review #11. | — |

### Week 13 · Jan 18 – 24 · Deploy to the cloud `[BOTH]`, `[FDE]` depth
| Day | Task | Done when |
|-----|------|-----------|
| Mon | Choose a target (Render / Fly.io / Railway / small VM); plan secrets, storage, and where the index lives. | 5-line deployment plan. |
| Tue | Deploy the container with HTTPS and a health check. | Public URL answers `/health`. |
| Wed | Persistent index storage; an ingestion/re-index job. | Re-index without downtime (or downtime documented). |
| Thu | Monitoring: error logs, uptime check, API-spend alert. | You'd know within 10 min if it broke. |
| Fri | **Quiz #12**. | — |
| Sat | `RUNBOOK.md`: deploy, roll back, rotate a key, re-index, top 5 errors and fixes. Test it from a clean clone. | **M8b done**. |
| Sun | Weekly review #12. | — |

### Week 14 · Jan 25 – 31 · Customer simulation `[FDE]` core, `[BOTH]` useful
**Scenario:** *"Acme Corp" wants your doc-QA over their internal docs (a folder of PDFs and HTML exports),
behind their SSO. Legal asks where data goes and how long it is kept. Their CTO asks "will it hallucinate?"*
| Day | Task | Done when |
|-----|------|-----------|
| Mon | Discovery: 10 questions you'd ask Acme; success criteria; a scope with explicit out-of-scope items. | `customer-sim/SCOPING.md`. |
| Tue | New connector: ingest PDF/HTML; incremental re-index of changed files only. | Changing one file re-indexes one file. |
| Wed | Security questionnaire: honestly answer 10 typical questions (data flow, LLM provider as subprocessor, retention, encryption, access control, logging). | `customer-sim/SECURITY_ANSWERS.md`. |
| Thu | Limitations memo: what it can't do, the measured failure rate, recommended human review. | 1 page, no hype. |
| Fri | **Quiz #13 (scenario):** "The customer says it's hallucinating. Walk me through what you do." | Logged. |
| Sat | Run your eval on the "customer" data, adapt (chunking/prompts), write a results report; record a 10-minute demo of yourself. | Report + recording. |
| Sun | Weekly review #13. | — |

---

## Phase 4 — Specialize and show it (Weeks 15–16)

### Week 15 · Feb 1 – 7 · Track deep dive (pick your lean)
| Day | `[AIE]` track | `[FDE]` track |
|-----|---------------|---------------|
| Mon | Compare 2 embedding models + 2 rerankers on your golden set. | Multi-tenant isolation: separate indexes vs a tenant filter. Trade-offs. |
| Tue | Structured extraction pipeline (docs → JSON) with its own eval. | PII redaction at ingestion and in logs. |
| Wed | Read: fine-tuning vs prompting vs RAG. When does each win? | Read: running models in a customer cloud (Bedrock / Vertex / Azure OpenAI), VPC and data residency. |
| Thu | Agent eval harness: tasks, graders, regression tracking. | Customer handoff doc for their IT team (architecture, ops, support boundaries). |
| Fri | **Quiz #14** | **Quiz #14** |
| Sat | Write up the deep dive with numbers. | Write up the deep dive with a diagram. |

### Week 16 · Feb 8 – 14 · Portfolio and interview readiness `[BOTH]`
| Day | Task | Done when |
|-----|------|-----------|
| Mon | README: problem, architecture, **eval numbers**, trade-offs, what you'd do next. | A stranger understands it in 2 minutes. |
| Tue | Write-up: "Naive RAG → hybrid → GraphRAG, with numbers" (blog post or long README section). | Published or committed. |
| Wed | System design practice: "RAG for 10k employees with permissions and SSO." | Written design, 1–2 pages. |
| Thu | 5 STAR stories from this repo (a bug you hunted, a limitation you communicated, a trade-off you measured). | `notes/stories.md`. |
| Fri | **Final quiz / mock interview** (cumulative). | — |
| Sat | Retrospective + plan the next 16 weeks. | — |

---

## Mastery checklist (the "can I explain it?" list)
Tracked in [`quizzes/QUIZ_BANK.md`](quizzes/QUIZ_BANK.md). A topic counts as mastered only when you've explained it
correctly **twice, at least a week apart, without notes**.

## After this plan (not before!)
MCP and tool ecosystems · fine-tuning / LoRA · multimodal RAG · LLM serving (vLLM) · advanced agent
architectures · cloud certifications (FDE).
