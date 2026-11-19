# Quiz Log

Newest on top. One row per question asked. Status changes also go in the mastery tracker in `QUIZ_BANK.md`.

| Date | Concept # | Question (short) | Grade | What was missing / correction | Next due |
|------|-----------|------------------|-------|-------------------------------|----------|
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
