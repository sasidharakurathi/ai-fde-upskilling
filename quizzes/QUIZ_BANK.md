# Quiz Rules and Mastery Tracker

> **Paused 2026-11-26 by choice:** no quizzes for now. Kept as history. Say "quiz me" any time to use it again.


## How quizzes work
- Questions come from each lesson's **Explain it back** section, plus extra questions from Claude that mix
  older topics in.
- Claude asks **one question at a time**. You answer in your own words, **without notes**.
- Claude grades it: 🟩 solid · 🟨 shaky · 🟥 missing. Then Claude explains what was right and what was
  missing, and logs it in `QUIZ_LOG.md`.
- **Mastered (✅)** = 🟩 twice, **at least 7 days apart**.

## Spacing (when a topic comes back)
| Last grade | Ask again in |
|------------|--------------|
| 🟥 missing | 2–3 days (after re-reading the lesson) |
| 🟨 shaky | about 1 week |
| 🟩 solid (first time) | 2–3 weeks |
| ✅ mastered | Only in mixed reviews and mock interviews |

**When:** Fridays (this week's lessons + anything due), Sundays (anything due), and whenever you ask.
No separate end-of-stage gate quizzes (dropped 2026-11-20).

## Mastery tracker
Rows are added **when a lesson is taught**, not before.
Status: ⬜ not quizzed · 🟥 missing · 🟨 shaky · 🟩 solid once · ✅ mastered

| Lesson | Concept | Status | Last quizzed | Next due |
|--------|---------|--------|--------------|----------|
| 0.1 | Rules vs machine learning | 🟩 | 2026-10-26 | 2026-11-20 |
| 0.1 | Training, model, inference | 🟨 | 2026-11-19 | 2026-11-26 |
| 0.1 | What an LLM does at its core (next-token prediction) | 🟩 | 2026-10-26 | 2026-11-20 |
| 0.1 | The circles: AI ⊃ ML ⊃ DL ⊃ GenAI ⊃ LLM | 🟩 | 2026-11-19 | 2026-12-08 |
| 0.1 | Other ways of doing AI: rules, search, logic vs ML | 🟩 | 2026-11-19 | 2026-12-08 |
| 0.2 | AI Engineer vs FDE: what each does day to day | 🟩 | 2026-10-26 | 2026-11-20 |
| 0.2 | What both roles share (the overlap) | 🟩 | 2026-10-26 | 2026-11-20 |
| 0.2 | Why FDEs must be honest about limits | 🟩 | 2026-11-19 | 2026-12-08 |
| 0.2 | AI researcher vs ML Engineer vs AI Engineer | 🟩 | 2026-10-26 | 2026-11-20 |
| 0.3 | The 7 parts of an AI app, in flow order | 🟩 | 2026-11-19 | 2026-12-08 |
| 0.3 | The model is stateless; apps re-send history | 🟩 | 2026-11-19 | 2026-12-08 |
| 0.3 | Debugging: data vs retrieval vs prompt vs model vs code | 🟩 | 2026-11-19 | 2026-12-08 |
| 0.3 | Which parts each role goes deepest on | 🟩 | 2026-11-19 | 2026-12-08 |
| 0.4a | Virtual environments: one toolbox per project | 🟩 | 2026-11-19 | 2026-12-08 |
| 0.4a | pyproject.toml vs uv.lock; what goes in git | 🟩 | 2026-11-19 | 2026-12-08 |
| 0.4a | Secrets: env vars, .env, .gitignore; revoke a leaked key first | 🟨 | 2026-11-19 | 2026-11-26 |
| 0.4a | Own .env parser vs python-dotenv (what the package hides) | 🟩 | 2026-11-19 | 2026-12-08 |
| 0.4b | HTTP request: URL, 3 headers, JSON body; status codes | 🟩 | 2026-11-20 | 2026-12-08 |
| 0.4b | Response: content blocks, stop_reason, usage | 🟩 | 2026-11-20 | 2026-12-08 |
| 0.4b | Tokens → cost (input vs output price) | 🟩 | 2026-11-20 | 2026-12-08 |
| 0.4b | Raw HTTP vs SDK: what the SDK does and hides | 🟨 | 2026-11-20 | 2026-11-27 |
| 1.1 | Example, label, feature (and why features are numbers) | ⬜ | — | after lesson |
| 1.1 | Look at the data first; imbalanced classes (13% spam) | ⬜ | — | after lesson |
| 1.1 | Own loader vs Hugging Face `datasets` (label encoding, cache) | ⬜ | — | after lesson |
