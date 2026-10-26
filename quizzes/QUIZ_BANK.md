# Quiz Bank and Mastery Tracker

**How quizzes work:** Claude asks **one question at a time**. You answer in your own words, without
notes. Claude grades it as 🟩 solid / 🟨 shaky / 🟥 missing, gives you a correction, and logs it in `QUIZ_LOG.md`.
- **Mastered (✅)** = 🟩 twice, at least 7 days apart.
- **Spacing:** 🟥 → re-ask in 2–3 days · 🟨 → next week · first 🟩 → in 2–3 weeks.
- Fridays: 3–5 questions on the week's topics + 1–2 that are due. Sundays: anything due.

## Mastery tracker

Status: ⬜ not yet quizzed · 🟥 missing · 🟨 shaky · 🟩 solid once · ✅ mastered

| # | Concept | Week | Status | Last quizzed | Next due |
|---|---------|------|--------|--------------|----------|
| 1 | Embeddings and cosine similarity | 1 | ⬜ | — | 2026-10-30 |
| 2 | RAG vs similarity search | 1 | ⬜ | — | 2026-10-30 |
| 3 | Tokens, context windows, cost | 1 | ⬜ | — | 2026-10-30 |
| 4 | Chunking trade-offs | 2 | ⬜ | — | — |
| 5 | Retrieval miss vs generation error | 2 | ⬜ | — | — |
| 6 | BM25 / keyword search | 3 | ⬜ | — | — |
| 7 | Hybrid search and Reciprocal Rank Fusion | 3 | ⬜ | — | — |
| 8 | Reranking (bi-encoder vs cross-encoder); vector stores and ANN | 3 | ⬜ | — | — |
| 9 | Citations, grounding, and "I don't know" | 4 | ⬜ | — | — |
| 10 | Prompt injection (direct and indirect) | 4 | ⬜ | — | — |
| 11 | Retrieval metrics: recall@k, hit rate, MRR | 5 | ⬜ | — | — |
| 12 | LLM-as-judge and how to trust it | 5 | ⬜ | — | — |
| 13 | Serving: API design, logging, containers, CI | 6 | ⬜ | — | — |
| 14 | Knowledge graph, triples, ontology vs similarity network | 7 | ⬜ | — | — |
| 15 | Entity extraction and entity resolution | 7 | ⬜ | — | — |
| 16 | GraphRAG (local vs global) and when it's worth it | 8 | ⬜ | — | — |
| 17 | Agents and tool calling; when NOT to use one | 10 | ⬜ | — | — |
| 18 | Cost, latency, caching, observability | 11 | ⬜ | — | — |
| 19 | AuthN/AuthZ, OIDC/SSO, permission-aware retrieval | 12 | ⬜ | — | — |
| 20 | AIE vs FDE; communicating limitations to a customer | 1, 14 | ⬜ | — | — |

## Question bank

**1. Embeddings and cosine similarity**
- What is an embedding, and why do texts with similar meaning get similar embeddings?
- What does cosine similarity measure? Why do we often normalize vectors first?
- Give two queries where pure embedding search fails, and say why.

**2. RAG vs similarity search**
- Explain RAG to a non-technical manager in 4 sentences.
- Your old app found similar documents with embeddings. Was that RAG? What would you add to make it RAG?
- Name two failure modes RAG has that similarity search doesn't.

**3. Tokens, context, cost**
- Why not just put the whole corpus in the prompt? Give at least 3 reasons.
- Estimate the monthly cost of 500 questions/day with 4,000 input tokens and 300 output tokens each, at the prices of the model you use.

**4. Chunking**
- What goes wrong with chunks that are too small? Too large? Why does overlap help?
- When would you split by headings instead of a fixed size?

**5. Retrieval miss vs generation error**
- A user gets a wrong answer. How do you tell whether retrieval or generation caused it? What do you check first?

**6. BM25**
- What three things does BM25 reward or penalise? Why does it beat embeddings on "ERR-4012"?

**7. Hybrid + RRF**
- Why fuse ranks instead of raw scores? Write the RRF formula from memory.

**8. Reranking + vector stores**
- Bi-encoder vs cross-encoder: which is used for first-stage retrieval, which for reranking, and why?
- What does an ANN index (like HNSW) trade away to be fast?

**9. Citations and grounding**
- How would you check automatically that a citation is valid? What can't the automatic check catch?
- How do you make a RAG system say "I don't know" reliably? Name two levers.

**10. Prompt injection**
- What's the difference between direct and indirect prompt injection? Why is indirect injection worse for RAG and agents?
- Name two mitigations, and explain why neither is complete.

**11. Retrieval metrics**
- Define recall@5 and MRR. Your recall@5 is 0.9 but answers are still bad. What's going on?

**12. LLM-as-judge**
- Why can't you just trust an LLM judge? How do you check whether it agrees with humans?

**13. Serving**
- What should and shouldn't go in your request logs? Why is ingestion a separate command from serving?

**14. Knowledge graphs**
- Knowledge graph vs similarity network: what's on the nodes, what's on the edges, and what questions can each answer?
- What is an ontology for? What happens if you extract triples with an LLM without one?

**15. Extraction and entity resolution**
- What is entity resolution? Give an example from your corpus. How did you handle it?

**16. GraphRAG**
- Explain local vs global GraphRAG.
- A customer with a 200-page FAQ asks for "GraphRAG because it's better." What do you say and do?
- Name 3 situations where GraphRAG is worth its cost.

**17. Agents**
- Workflow vs agent: what's the difference? When would you choose a fixed workflow?
- What guardrails does an agent loop need in production?

**18. Production**
- p50 vs p95 latency: which do users feel? Name 3 ways to cut cost without hurting quality much.

**19. Auth and permissions**
- AuthN vs AuthZ in one sentence each. What does SSO via OIDC give a customer?
- Why must permission filtering happen *before* ranking and generation? How can a cache leak data?

**20. Roles and communication**
- AI Engineer vs FDE: main question, typical day, key artefacts.
- The customer's CTO asks "Will it hallucinate?" Give your honest 30-second answer.
- The customer says "it's giving wrong answers." Walk through your first hour.
