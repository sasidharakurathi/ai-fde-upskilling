# Core Concepts — Reference Sheet

> **Don't read this yet.** These topics are taught step by step, in simple English, in the
> lessons: embeddings (2.3, 5.1), RAG (5.3–5.10), knowledge graphs (8.1–8.5), GraphRAG (8.6), and roles (0.2, 14).
> Come back here **after** those lessons, as a one-page summary to revise from.

---

## 1. Embeddings and similarity search (what you probably built before)

**An embedding** is a list of numbers (a vector, e.g. 384 or 1536 numbers) that an *embedding model*
produces for a piece of text. The model is trained so that texts with similar **meaning** end up
with vectors that point in similar directions.

```
"How do I reset my password?"     -> [0.12, -0.40, 0.88, ...]
"I forgot my login credentials"   -> [0.10, -0.38, 0.91, ...]   <- close (similar meaning)
"Best pizza in Naples"            -> [-0.70, 0.22, 0.05, ...]   <- far away
```

**Similarity search** (also called *semantic search* or *vector search*):

1. Embed every document (or chunk) once and store the vectors.
2. When a query comes in, embed it with the same model.
3. Compare the query vector to the stored vectors. The usual measure is **cosine similarity**, the
   cosine of the angle between two vectors: 1 means the same direction and 0 means unrelated.
4. Return the **top-k** closest documents.

**Output: a ranked list of documents.** That's all. Nothing gets written, summarised, or answered.
A "similar products" or "related articles" feature is this.

Where pure embedding search fails (you'll see these yourself in Lesson 5.2):
- **Exact identifiers**: error codes, product SKUs, names ("ERR-4012"). Embeddings blur these.
- **Negation**: "policies that do *not* apply to contractors" usually embeds close to the policies
  that *do* apply.
- **Domain jargon** the embedding model never saw much of.

---

## 2. RAG — Retrieval-Augmented Generation

RAG = **R**etrieve relevant text → **A**ugment the prompt with it → have an LLM **G**enerate an answer
grounded in that text.

```
question ──► [Retriever] ──► top-k chunks ──► [Prompt: "Answer using ONLY these sources..."
                                                        + chunks + question]
                                                              │
                                                              ▼
                                                           [LLM] ──► answer + citations
```

### RAG vs "embeddings to find similar documents"

|                     | Similarity search                | RAG                                                   |
|---------------------|----------------------------------|-------------------------------------------------------|
| Output              | A list of documents              | A written **answer** (ideally with citations)         |
| Uses an LLM?        | No (only an embedding model)     | Yes, to generate the answer                           |
| Uses embeddings?    | Always                           | **Optional**. The retriever can be keyword (BM25), hybrid, SQL, a graph, or an API call |
| Main failure        | Wrong documents ranked high      | Wrong documents **or** right documents but a wrong or made-up answer |
| What you evaluate   | Retrieval quality                | Retrieval quality **and** generation quality, separately |

**Key insight:** similarity search is often *one component inside* RAG (the retriever). RAG adds
a second stage with its own problems:

- **Chunking**: documents are too long, so you split them. Bad splits lose context.
- **Context window and cost**: you can only fit so many chunks in the prompt, and every token costs money.
- **Faithfulness**: the LLM may ignore the sources and make things up (hallucinate).
- **Citations**: users (and customers!) need to check where each claim came from.
- **No-answer handling**: when the sources don't contain the answer, the system should say
  "I don't know," not guess.

**Hybrid search** = run keyword search (BM25, good at exact terms) *and* vector search (good at
meaning), then merge the two rankings, usually with *Reciprocal Rank Fusion*. It's the standard
strong baseline.

---

## 3. Knowledge graph vs similarity network

Both are "graphs" (nodes + edges), but they mean completely different things.

### Similarity network
- **Nodes:** documents (or items).
- **Edges:** "these two are similar," with a weight (e.g. cosine 0.83). **Every edge is the same kind.**
- Built **automatically** from embeddings (e.g. connect pairs with similarity > 0.8).
- Edges are usually undirected, and *why* two things are connected is never stated.
- Answers: "What's like this?" and "What clusters exist?"

### Knowledge graph (KG)
- **Nodes:** **entities** with **types**: `Person: Alice`, `Team: Platform`, `Policy: Remote Work`.
- **Edges:** **typed, directed relationships**: `Alice —MANAGES→ Platform`,
  `Remote Work —APPLIES_TO→ Contractors`.
- Each fact is a **triple**: `(subject, predicate, object)`.
- Answers **structured and multi-hop** questions: *"Which policies apply to the team Alice manages?"*
  → walk `Alice → MANAGES → Platform → (policies that APPLY_TO Platform)`.

```
Similarity network:              Knowledge graph:

  [Doc A]──0.83──[Doc B]           (Alice:Person) ──MANAGES──► (Platform:Team)
     │                                                              ▲
    0.79                           (On-call Policy:Policy) ─APPLIES_TO┘
     │
  [Doc C]                          Types and edge meanings are explicit.
  Edges only mean "similar".
```

### Ontology (and schema)
An **ontology** is the formal *vocabulary and rules* of a KG:
- which **entity types** exist (`Person`, `Team`, `Policy`, `Tool`);
- which **relationship types** exist and between which types (`MANAGES: Person → Team`,
  `USES: Team → Tool`);
- optionally, hierarchy and constraints (`Manager` is a kind of `Person`; a Team has exactly one manager).

In practical LLM work you mostly need a lightweight **schema**: a short list of allowed entity and
relationship types. Without one, LLM extraction gives you a messy graph (`manages`, `is manager of`,
`leads`, `heads` all as different edges).

**Hard parts of KGs:** extraction errors, **entity resolution** ("Alice Chen" = "A. Chen" = "Alice"),
and keeping the graph up to date when documents change.

---

## 4. GraphRAG — and when it's worth it

**GraphRAG** = RAG where a **graph** (usually a knowledge graph) is part of retrieval. There are two
common flavours:

1. **Local / traversal GraphRAG**: find the entities mentioned in the question, look them up in the
   KG, walk 1–2 hops to their neighbours, and put the facts **plus the source chunks those facts came from**
   in the prompt. This is good for relationship and **multi-hop** questions.
2. **Global GraphRAG** (popularised by Microsoft's 2024 "GraphRAG" paper): an LLM extracts entities
   and relationships from the whole corpus, a community-detection algorithm groups related entities into
   clusters, and the LLM pre-writes a **summary per community**. Corpus-wide questions ("What are the
   main themes / risks across all these documents?") are answered by combining the community summaries.
   Plain RAG does badly here because no single chunk holds the answer.

### When it's worth it
- Questions are about **relationships across documents** (who/what is connected to what).
- **Multi-hop** questions that need facts from several places chained together.
- **Global / summarise-everything** questions over a large corpus.
- Domains with clear entities: org structures, supply chains, legal contracts, biomedical, IT
  systems and dependencies.
- You **already have structured data** (a CMDB, org chart, or database) that gives you a graph cheaply.

### When it's NOT worth it (most cases, honestly)
- Most questions can be answered from **one or two chunks** (FAQs, support docs, policies).
- Small corpus, fast-changing data (re-extraction is expensive), or tight budget. Indexing calls the LLM
  on every chunk.
- **You haven't measured that hybrid search + reranking fails.**

**The rule you'll follow in this plan:** build hybrid search first → build an eval set → find which
question types fail → add a graph only for those, and **measure** whether it helped. You'll do
exactly this in Stages 6 and 8.

---

## 5. AI Engineer vs Forward Deployed Engineer (FDE)

Titles vary by company. These are the typical shapes.

**AI Engineer: builds the AI system.**
RAG pipelines, agents and tool use, prompt design, **evals**, model selection, cost and latency
trade-offs, sometimes fine-tuning. Usually sits on a product or platform team. Success = *the system
measurably works well* (eval scores, quality, cost).

**Forward Deployed Engineer: makes it work inside a specific customer's world.**
Embedded with customers (the title comes from Palantir and is now common at AI companies). You take the
product into the customer's environment: connect their data sources, plug into their **SSO/auth** and
permission model, get through their **security review**, work within network and compliance limits,
adapt workflows, debug in production, scope what's feasible, report needs back to the product team, and
**tell the customer honestly what the system can't do**. Success = *the customer gets real value in
production*. Lots of writing and talking; breadth over depth.

|                       | AI Engineer                          | FDE                                                  |
|-----------------------|--------------------------------------|------------------------------------------------------|
| Main question         | "How do we make the system good?"    | "How do we make it work *here*, for *them*?"         |
| Typical day           | Run evals, tune retrieval, build agent | Customer call, integration, auth issue, demo, write-up |
| Depth vs breadth      | Deep on LLM systems                  | Broad: auth, networking, data, security, people      |
| Key artefacts         | Eval reports, pipelines, prompts     | Runbooks, scoping docs, security answers, demos      |
| Hardest skill         | Measuring and improving quality      | Ambiguity + honest communication under pressure      |

**Overlap (what this plan marks `[BOTH]`):** Python and APIs, building RAG end to end, **evals** (an FDE
must prove it works on *this customer's* data), debugging, deployment basics, security awareness
(prompt injection, data leakage, permissions), and clear writing.

**How you'll choose:** Stages 0–7 are almost entirely `[BOTH]`. Notice which work you
enjoy more: tuning retrieval and reading eval tables (AI Engineer), or getting it deployed, secured,
and explained (FDE). At the role checkpoint after Stage 7 you'll pick a lean, not a cage.
