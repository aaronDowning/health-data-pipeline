---
title: Homelab Lab School — Progress Log
program: SYLLABUS.md
protocol: SESSION-PROTOCOL.md
started: 2026-06-01
---

# Progress Log

The session protocol updates this file after every lesson. Three live sections drive the system:
**Current Position** (cold resume), **Revisit Queue** (spaced repetition), and **Entries** (retros).

---

## 📍 Current Position

> Where we resume next session. Updated at the LOG step every time.

- **Module:** 0 — Project setup & CI skeleton
- **Lesson:** 0.3 — First pytest (not yet started)
- **Stopped at:** 0.2 complete — venv rebuilt on Homebrew Python 3.12, pytest installed, requirements.txt pinned via pip freeze. Also fixed the foundation: installed a real Python via Homebrew instead of relying on Apple's system 3.9.
- **Next up:** Lesson 0.3 — write and run the first pytest, green locally.

---

## 🔁 Revisit Queue (spaced repetition)

> Concepts that were shaky. Re-quizzed at the RECALL step until solid, then removed.
> Hard-gate failures land here.

_(empty — nothing learned yet)_

---

## Status at a glance

| Module | Title | Status | Date done |
|---|---|---|---|
| 0 | Project setup & CI skeleton | 🟡 In progress (0.1, 0.2 ✅) | — |
| 1 | Python ETL fundamentals | ⬜ Not started | — |
| 2 | Postgres warehouse + SQL depth | ⬜ Not started | — |
| 3 | Synthetic healthcare data (Synthea/FHIR/REDCap) | ⬜ Not started | — |
| 3.5 | NoSQL document store (MongoDB) — required-quals gap | ⬜ Not started | — |
| 4 | Airflow orchestration | ⬜ Not started | — |
| 5 | Spark / PySpark | ⬜ Not started | — |
| 6 | Data lake / lakehouse (MinIO) | ⬜ Not started | — |
| 7 | Data quality & testing | ⬜ Not started | — |
| 7.5 | Analytics dashboard (optional) | ⬜ Not started | — |
| 8 | CI/CD for the pipeline | ⬜ Not started | — |
| 9 | Capstone & demo | ⬜ Not started | — |

Status key: ⬜ Not started · 🟡 In progress · ✅ Done · 🔁 Needs revisit

---

## Retro template (Claude copies this per lesson at the LOG step)

### Module N · Lesson N.M — <title>
- **Date(s):**
- **What we built:**
- **What clicked / went well:**
- **What was hard / confusing:**
- **Gate result:** engineer-explain ☐ · stakeholder-explain ☐ (both ✓ to advance)
- **Revisit later (→ Revisit Queue):**
- **Talking point — can I say it confidently? (y/n):**
- **Next step:**

---

# Entries

### Module 0 · Lesson 0.1 — Repo & project structure
- **Date(s):** 2026-06-03
- **What we built:** `health-data-pipeline` repo — `src/`, `tests/`, `README.md`, `.gitignore` (with a healthcare PHI guardrail); git init + first commit + pushed to GitHub (private).
- **What clicked / went well:** Mapped instantly to his own `atxn-qa-framework` — recognized the work/proof/docs structure cold. Prior framework experience transferred directly.
- **What was hard / confusing:** Nothing — known territory.
- **Gate result:** engineer-explain ✓ · stakeholder-explain ✓ (recitation waived — demonstrably knew it from building frameworks)
- **Revisit later (→ Revisit Queue):** none
- **Talking point — can I say it confidently? (y/n):** y — "I scaffolded the repo with clean structure and a HIPAA-safe `.gitignore` from commit one."
- **Next step:** 0.2 — dependencies & venv.

### Module 0 · Lesson 0.2 — Dependencies & venv (plus a 0.0 Python-foundation fix)
- **Date(s):** 2026-06-03
- **What we built:** Caught that the machine only had Apple's system Python 3.9, so first installed Homebrew Python 3.12. Rebuilt the project venv on 3.12, installed pytest, and pinned exact versions into `requirements.txt` via `pip freeze`.
- **What clicked / went well:** Mapped venv to `node_modules` + `package.json` instantly; predicted transitive dependencies correctly before running; caught the missing real-Python foundation himself (sharp QA instinct).
- **What was hard / confusing:** Nothing conceptual; the only gap was the machine having just system Python, now resolved.
- **Gate result:** engineer-explain ✓ · stakeholder-explain ✓ (recitation waived — shown via correct prediction + hands-on)
- **Revisit later (→ Revisit Queue):** none
- **Talking point — can I say it confidently? (y/n):** y — "Each project gets an isolated venv with a pinned requirements file, so it installs identically on my machine and in CI."
- **Next step:** 0.3 — first pytest.
