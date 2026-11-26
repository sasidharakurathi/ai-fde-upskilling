# Daily Check-ins

Newest entry at the top. **Claude writes these** when you say "X done" (or what you did).

```markdown
## YYYY-MM-DD (Day) · Lesson # · <status ✅/🟡/💤/❌>
- **Planned:** <lesson # or project task>
- **Did:** <what actually happened, 1–2 lines>
- **Time:** <minutes>
- **In my own words:** <one sentence about something I learned>
- **Stuck on:** <or "nothing">
- **First step tomorrow (≤ 5 min):** <very concrete, e.g. "open retrieve.py and write the function signature for search()">
```

---

<!-- entries go below this line, newest first -->

## 2026-11-26 (Thu) · Lesson 1.1 · ✅ (back after 5 days)
- **Planned:** Lesson 1.1: download the SMS Spam Collection, look at it, build features, compare with Hugging Face `datasets`.
- **Did:** Both loaders work (5,574 messages, 13.4% spam). Feature table built, plus 2 own features (`has_http_or_www`, `capital_to_length_ratio`). Strongest clue: digits (15.8 spam vs 0.3 ham). Changed the way of working: Claude now writes all notes; no quizzes or explain-backs.
- **Time:** (not reported)
- **Notes:** `notes/lesson-notes.md` → 1.1 · compare: `projects/classifier/NOTES.md`
- **First step tomorrow (≤ 5 min):** Open `lessons/1.2-training-and-inference.md`, read "What you'll build", then create the empty file `projects/classifier/sms_data.py`.

## 2026-11-20 (Fri) · Lesson 0.4b · ✅
- **Planned:** Lesson 0.4b: first LLM call, raw `httpx` then the SDK (guided build).
- **Did:** First real Claude API calls 🎉: raw + SDK scripts work, with tokens and cost printed; SDK errors caught with try/except; break-it tests; compare notes; explain-back. No key in git ✓. **Project P0 done.**
- **Time:** ~60 min
- **In my own words:** The SDK builds the URL, headers and JSON for me; the raw version shows exactly what travels over the internet.
- **Stuck on:** the lesson first said *what* to do but not *how*. Rewritten as a guided build.
- **First step tomorrow (≤ 5 min):** Add `Correction:` lines for 0.4b Q3 and the NOTES compare. Then (Saturday build block) fix `00a_read_env.py` for the tricky lines in Lesson 0.4a Step 2b.

## 2026-11-19 (Thu, extra lesson) · Lesson 0.4a · ✅
- **Planned:** Extra lesson on a good day: Lesson 0.4a (workspace, secrets, git habits).
- **Did:** uv project + .gitignore set up (no .env or .venv in git ✓); own .env reader + python-dotenv version; NOTES.md compare; explain-back.
- **Time:** ~60 min
- **In my own words:** Each project gets its own .venv toolbox; pyproject.toml is the shopping list, uv.lock the exact receipt.
- **Stuck on:** nothing. (Found later: own .env reader crashes on 3 common line types; see grades.)
- **First step tomorrow (≤ 5 min):** Add the 3 `Correction:` lines for 0.4a (Q3, Q4, NOTES.md line 2). Then Friday quiz with Claude, then Lesson 0.4b.
- **Saturday build block idea:** fix `experiments/00a_read_env.py` so the 4 failing cases from Claude's review work.

## 2026-11-19 (Thu) · RESTART · ✅
- **Planned:** Restart protocol: re-read Lesson 0.2, 20-min review quiz on 0.1–0.2, then Lesson 0.3 if there's energy left.
- **Did:** Came back after a 23-day gap. Restart quiz: 3 🟩, 1 🟨, no 🟥. Then Lesson 0.3: Part A all 7 steps, Part B 6/6 with whys, explain-back all 🟩.
- **Time:** ~20 min (quiz) + Lesson 0.3 ~50 min
- **In my own words:** Search tries options until the rules (the goal) are met, like a Sudoku solver.
- **Stuck on:** nothing
- **First step tomorrow (≤ 5 min):** Friday quiz with Claude (a few due 🟩 topics), then open `lessons/0.4a-workspace-and-secrets.md` and run `uv --version`.

## 2026-10-26 (Mon, extra lesson) · Lesson 0.2 · ✅
- **Planned:** Extra lesson on a good day: corrections for 0.1, then Lesson 0.2 (AI Engineer vs FDE).
- **Did:** 3 corrections for 0.1 written; Lesson 0.2 sorting 10/10; 4 explain-back answers.
- **Time:** ~54 min
- **In my own words:** An AI Engineer builds the AI product; an FDE makes it work inside each customer's environment and brings their feedback back.
- **Role signal:** most fun tasks were 1, 3, 9 (+6): testing prompts, comparing models, designing agents, building RAG. All AI-Engineer-flavoured. Early signal only.
- **Stuck on:** nothing
- **First step tomorrow (≤ 5 min):** Add the `Correction:` line under 0.2 answer 3 (a concrete example of what goes wrong), then read just the "Ask HR" diagram at the top of `lessons/0.3-parts-of-an-ai-app.md`.

## 2026-10-26 (Mon) · Lesson 0.1 · ✅
- **Planned:** Lesson 0.1, AI vs ML vs DL vs GenAI vs LLM.
- **Did:** Read the lesson, asked about "other ways of doing AI" (rules, search, logic), sorting 9/9, all 4 explain-back answers written and pushed. Also set up the full plan with Claude.
- **Time:** ~60 min
- **In my own words:** ML learns patterns from labelled examples instead of hand-written rules (e.g. detecting adult sites).
- **Stuck on:** what "ML is one way of doing AI" means. Resolved (rules, search, logic, ML).
- **First step tomorrow (≤ 5 min):** Add the 2 `Correction:` lines for Lesson 0.1 in `notes/my-words.md`, then read just the coffee-machine story at the top of `lessons/0.2-aie-vs-fde.md`.
