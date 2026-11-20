# Quiz Log

Newest on top. One row per question asked. Status changes also go in the mastery tracker in `QUIZ_BANK.md`.

| Date | Concept # | Question (short) | Grade | What was missing / correction | Next due |
|------|-----------|------------------|-------|-------------------------------|----------|
| 2026-11-20 | 0.4b | Code: raw httpx + SDK scripts (incl. "your turn" parts) | 🟩 | Both work; try/except in SDK version. Hints (not graded): use the INPUT_PRICE/OUTPUT_PRICE variables instead of typing 4.00/20.00 in the formula; `os.environ[...]` fails fast on a missing setting, `.get()` hides it until the API complains. | — |
| 2026-11-20 | 0.4b | NOTES compare (0.4b) | 🟨 | Covered what the SDK does and which to use. Missing two asked items: lines of code per version, and *how each showed the errors* in Step 3b. Nuance: the SDK doesn't "handle" errors, it raises typed exceptions that you still catch. | 2026-11-27 |
| 2026-11-20 | 0.4b | 3 headers | 🟩 | — | 2026-12-08 |
| 2026-11-20 | 0.4b | Input vs output tokens, cost formula | 🟩 | Correctly included thinking in output tokens. | 2026-12-08 |
| 2026-11-20 | 0.4b | Two things the SDK did; one thing it hid | 🟨 | Two things ✓ (key + headers). "Hid the key" isn't it (the key is in .env either way). It hid the URL, the headers/API version, the raw JSON, and automatic retries. | 2026-11-27 |
| 2026-11-20 | 0.4b | stop_reason "max_tokens" | 🟩 | Meaning ✓, fixes ✓. Extra tip: at runtime, check stop_reason and never show a cut-off answer as if complete. | 2026-12-08 |
| 2026-11-19 | 0.4a | **Regrade:** own .env reader | 🟩 | Met everything the lesson asked. The edge cases were never stated or given as tests, so they don't count against it (coach's mistake, fixed in the lesson). | — |
| 2026-11-19 | 0.4a | **Regrade:** NOTES compare + Q4 | 🟩 | Fair answer given the tests the lesson provided; correction now names the edge cases the package hides. | 2026-12-08 |
| 2026-11-19 | 0.4a | Correction: Q3 leaked key | ✓ | Now: revoke first, then clean up. | 2026-11-26 |
| 2026-11-19 | 0.4a | Try it: setup (uv, .gitignore, no secrets in git) | 🟩 | All correct; .env never committed. Optional cleanup: `src/` + `[build-system]`/`[project.scripts]` aren't needed. | — |
| 2026-11-19 | 0.4a | Own .env reader | 🟨 | Handles quotes + trailing comment (better than the reference!). Fails on: line without `#` (crash), blank line (crash), `=` in value (crash), `#` inside quotes (silently wrong: "pa"). | 2026-11-26 |
| 2026-11-19 | 0.4a | NOTES compare: what the package hid | 🟨 | Wrote "no difference". The 4 edge cases above are exactly what dotenv hides (+ `export`, multi-line, no override of existing vars). | 2026-11-26 |
| 2026-11-19 | 0.4a | Virtual env, one per project | 🟩 | — | 2026-12-08 |
| 2026-11-19 | 0.4a | pyproject.toml vs uv.lock; what goes in git | 🟩 | Key idea: lock = exact versions so every machine gets the same setup. | 2026-12-08 |
| 2026-11-19 | 0.4a | Why keys stay out of git; first step if leaked | 🟨 | Order: **revoke first**. Deleting the commit isn't enough (history, forks, bots copy keys within minutes). | 2026-11-26 |
| 2026-11-19 | 0.4a | Two things dotenv handled that mine didn't | 🟨 | Gave what both do (read + load). Answer = edge cases: lines without comments, blank lines, `=` in values, `#` inside quotes. | 2026-11-26 |
| 2026-11-19 | 0.3 | Part A: trace the shoe-returns question | 🟩 | All 7 parts in order, each with what it does. Tiny add: the answer goes back to the user at the end. | — |
| 2026-11-19 | 0.3 | Part B: detective (6 problems) | 🟩 6/6 | All with whys. Nice extra: using guardrails as a safety net. For #6, also ask why the bot could see card numbers at all (data/access). For #4 the main fault is the code (it builds the prompt). | — |
| 2026-11-19 | 0.3 | Parts in flow order | 🟩 | UI → code → data → prompt → model → checks → logs/evals. | 2026-12-08 |
| 2026-11-19 | 0.3 | Stateless model; how chat apps remember | 🟩 | Precise wording: the model never had memory (each call is independent); the code re-sends history, so long chats cost more tokens. | 2026-12-08 |
| 2026-11-19 | 0.3 | 3 parts that can cause wrong answers | 🟩 | Data, prompt, model. Also retrieval (found the wrong text) and code. Add a one-line example each next time. | 2026-12-08 |
| 2026-11-19 | 0.3 | What each role cares most about | 🟩 | Good. AIE side: also evals and prompt testing. | 2026-12-08 |
| 2026-11-19 | 0.2 | Restart Q4: hospital asks "fully replace staff?" (90% accurate) | 🟩 | Honest no + human-in-the-loop + benefit. Stronger with the number (1 in 10 wrong) and the why (patient harm). | 2026-12-08 |
| 2026-11-19 | 0.1 | Restart Q3: DL-not-GenAI and GenAI-not-LLM examples | 🟩 | Face unlock; image/video generators. Correct, but the whys were missing. | 2026-12-08 |
| 2026-11-19 | 0.1 | Restart Q2: Sudoku solver, which way of AI? | 🟩 | Search, with the why (tries options until the rules are met). Improved from the timetable answer. | 2026-12-08 |
| 2026-11-19 | 0.1 | Restart Q1: what is a model; contains / doesn't | 🟨 | "Learned patterns, not training data" ✓. Missing *what it is*: the output of training, a file of learned numbers that turns input into output. | 2026-11-26 |
| 2026-10-26 | 0.2 | Correction: honesty about limits | ✓ | Good concrete example: finance company, wrong interest rate; honest "95% correct, add human review". Re-check as planned. | 2026-11-02 |
| 2026-10-26 | 0.2 | Sorting 10 tasks AIE / FDE / BOTH | 🟩 10/10 | — | — |
| 2026-10-26 | 0.2 | AIE vs FDE in 3 sentences | 🟩 | Core difference right. Small fixes: agents are built *with* LLMs (not an alternative); no own analogy given. | 2026-11-12 |
| 2026-10-26 | 0.2 | 3 things both roles do | 🟩 | Python, RAG, debugging slowness. | 2026-11-12 |
| 2026-10-26 | 0.2 | Why FDEs must be honest about limits | 🟨 | Right direction but vague ("cause any issue"). Needs a concrete harm: users act on wrong answers, trust/contract lost, legal risk; and honesty lets the customer add safeguards (human review). | 2026-11-02 |
| 2026-10-26 | 0.2 | Researcher vs ML Eng vs AI Eng | 🟩 | Correct. Researchers invent new *methods*, not only train models. | 2026-11-12 |
| 2026-10-26 | 0.1 | Corrections for 3 🟨 answers | ✓ | Model = learned patterns, not training data · AI-only example = Maps route · modern LLMs also read images. All good. | — |
| 2026-10-26 | 0.1 | Fraud detector from 1M labelled payments: which way of AI? | 🟩 | Correct, with the why (learns patterns from data). Bonus: the "fraud / not fraud" labels make it *supervised* learning (Lesson 1.3). | 2026-11-12 |
| 2026-10-26 | 0.1 | Exam timetable: which way of AI? | 🟨 | Answered "rules" with no why. Best answer: search/planning. The rules (no clashes) describe the goal, but the computer must *try many arrangements* to find one that fits. Always give the why. | 2026-11-02 |
| 2026-10-26 | 0.1 | Sorting 9 examples into circles | 🟩 9/9 | — | — |
| 2026-10-26 | 0.1 | Rules vs ML, own example | 🟩 | Strong own example (adult-site detection), mentions confidence score. | 2026-11-12 |
| 2026-10-26 | 0.1 | Training / model / inference | 🟨 | Model ≠ stored training data: it's learned numbers (patterns), and only big models have billions. Inference = using a *trained* model. | 2026-11-02 |
| 2026-10-26 | 0.1 | What an LLM does; "it looked it up" | 🟩 | Small add: the LLM also uses whatever text is in the prompt; the app (not the LLM) runs the search tool. | 2026-11-12 |
| 2026-10-26 | 0.1 | The circles + own examples | 🟨 | Order correct. "Weather prediction" doesn't separate AI from ML (and classic forecasting is physics simulation, not AI); use a rules/search example for AI-only. LLMs: language models, many now also *read* images. | 2026-11-02 |
