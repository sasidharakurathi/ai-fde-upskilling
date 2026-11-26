# P1 · Classifier: notes and comparisons

*Written by Claude from running your code. Revision notes for each lesson: `notes/lesson-notes.md`.*

## Compare (1.1): own loader ① vs Hugging Face `datasets` ②
| Test | ① `01_explore.py` | ② `02_load_with_datasets.py` |
|------|-------------------|------------------------------|
| Messages | 5,574 | 5,574 |
| Label | `"ham"` / `"spam"` | `0` / `1` (label encoding; names in `ds.features["label"]`) |
| First message identical? | — | **No**: `datasets` adds `\n` to the end of every message |
| Same order? | — | Yes |
| Where stored | `data/sms/` (you chose) | Hugging Face cache (`~/.cache/huggingface/`) |
| Lines of code | ~35 for loading | 3 |

**What `datasets` did for you:** download, unzip, parse, cache, and label encoding.
**What it hid:** where the file lives, the label-to-number mapping, and the extra `\n` it adds.
**At work:** `datasets` for well-known public datasets; your own loader for a **customer's** files, which are never on
Hugging Face and are always messy.
