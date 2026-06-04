---
title: Lab School — Progress Log
program: SYLLABUS.md
protocol: SESSION-PROTOCOL.md
design: DESIGN.md
started: 2026-06-01
---

# Progress Log

The session protocol updates this file after every lesson. Three live sections drive the system:
Current Position (cold resume), Revisit Queue (spaced repetition), and Entries (retros).

## Current Position

> Where we resume next session. Updated at the LOG step every time.

* Module: 1, Python ETL fundamentals
* Lesson: 1.3, Transform clean (not yet started)
* Stopped at: 1.2 complete. Wrote src/extract.py (read_json) and a synthetic, messy sample_data/patients.json; verified it reads 3 records into a list of dicts. Module 0 lesson 0.5 (docker-compose) deferred to Module 2.
* Next up: Lesson 1.3, the first transform: clean the raw rows (trim whitespace, fix casing, handle nulls).

## Revisit Queue (spaced repetition)

> Concepts that were shaky. Asked again at the RECALL step until solid, then removed.
> Hard gate failures land here.

Empty.

## Status at a glance

| Module | Title | Status | Date done |
|---|---|---|---|
| 0 | Project setup and CI skeleton | 0.1 to 0.4 done; 0.5 deferred to Module 2 |  |
| 1 | Python ETL fundamentals | In progress (1.1, 1.2 done) |  |
| 2 | Postgres warehouse and SQL depth | Not started |  |
| 3 | Synthetic healthcare data (Synthea/FHIR/REDCap) | Not started |  |
| 3.5 | NoSQL document store (MongoDB) | Not started |  |
| 4 | Airflow orchestration | Not started |  |
| 5 | Spark / PySpark | Not started |  |
| 6 | Data lake / lakehouse (MinIO) | Not started |  |
| 7 | Data quality and testing | Not started |  |
| 7.5 | Analytics dashboard (optional) | Not started |  |
| 8 | CI/CD for the pipeline | Not started |  |
| 9 | Capstone and demo | Not started |  |

Status key: Not started, In progress, Done, Needs revisit.

## Retro template (copied per lesson at the LOG step)

### Module N · Lesson N.M: <title>
* Date(s):
* What we built:
* What clicked / went well:
* What was hard / confusing:
* Gate result: engineer explain (pass/fail), stakeholder explain (pass/fail). Both pass to advance.
* Revisit later (to Revisit Queue):
* Key takeaway:
* Next step:

# Entries

### Module 0 · Lesson 0.1: Repo and project structure
* Date(s): 2026-06-03
* What we built: the `health-data-pipeline` repo. `src/`, `tests/`, `README.md`, `.gitignore` (with a healthcare PHI guardrail); git init, first commit, pushed to GitHub.
* What clicked / went well: mapped instantly to a framework structure I already knew (work, proof, docs). Prior experience transferred directly.
* What was hard / confusing: nothing, known territory.
* Gate result: engineer explain pass, stakeholder explain pass.
* Revisit later: none.
* Key takeaway: "I scaffolded the repo with clean structure and a HIPAA safe `.gitignore` from commit one."
* Next step: 0.2, dependencies and venv.

### Module 0 · Lesson 0.2: Dependencies and venv (plus a 0.0 Python foundation fix)
* Date(s): 2026-06-03
* What we built: installed a Homebrew managed Python 3.12 (the machine only had the macOS system 3.9). Rebuilt the project venv on 3.12, installed pytest, and pinned exact versions into `requirements.txt` via `pip freeze`.
* What clicked / went well: mapped venv to node_modules plus package.json instantly; predicted transitive dependencies correctly before running; caught the missing real Python foundation myself.
* What was hard / confusing: nothing conceptual; the only gap was the machine having just the system Python, now resolved.
* Gate result: engineer explain pass, stakeholder explain pass.
* Revisit later: none.
* Key takeaway: "Each project gets an isolated venv with a pinned requirements file, so it installs identically on my machine and in CI."
* Next step: 0.3, first pytest.

### Module 0 · Lesson 0.3: First pytest
* Date(s): 2026-06-03
* What we built: `src/transforms.py` (clean_name), `pytest.ini` (pythonpath src, testpaths tests), and the first test `tests/test_1.py`. Result: 1 passed, green.
* What clicked / went well: home field. Grasped the differences from JS runners instantly (bare assert, convention discovery, no describe or it). Wrote an edge case test and surfaced a real bug in clean_name via title casing.
* What was hard / confusing: nothing conceptual. The failing test was a genuine code limitation, not a misunderstanding.
* Gate result: engineer explain pass, stakeholder explain pass.
* Revisit later: none. Code finding logged to BACKLOG, not the queue.
* Key takeaway: "I write pytest with plain asserts and convention discovery, and I catch data corrupting edge cases early."
* Next step: 0.4, wire pytest into GitHub Actions.

### Module 0 · Lesson 0.4: GitHub Actions CI
* Date(s): 2026-06-04
* What we built: `.github/workflows/ci.yml`. Runs on push and pull request, sets up Python 3.12, installs the pinned requirements, runs pytest on a clean runner. First run completed green in 17 seconds.
* What clicked / went well: home field. Predicted the behavior correctly. The only new piece was the GitHub Actions UI tab and the Python flavor of the steps (setup-python, pip install, pytest) versus the JS equivalents.
* What was hard / confusing: nothing; CI is a core strength.
* Gate result: engineer explain pass, stakeholder explain pass.
* Revisit later: none.
* Key takeaway: "My repo has CI gating from the first commit: every push runs the tests on a clean runner, a failing check blocks the change."
* Next step: 0.5, docker-compose skeleton.

### Module 1 · Lesson 1.1: The ETL model
* Date(s): 2026-06-04
* What we built: no code; a concept lesson. Mapped the planned pipeline to E, T, L (reading FHIR is Extract, flattening and de identifying is Transform, writing to Postgres is Load).
* What clicked / went well: mapped all three correctly on the first try, and identified Transform as the highest code and risk stage with a sharp QA framing: changing data is where it can be mutated incorrectly.
* What was hard / confusing: nothing.
* Gate result: engineer explain pass, stakeholder explain pass.
* Revisit later: none.
* Key takeaway: "ETL is extract, transform, load; the transform stage holds the most code and risk, and a QA mindset there keeps the pipeline trustworthy."
* Next step: 1.2, Extract.

### Module 1 · Lesson 1.2: Extract
* Date(s): 2026-06-04
* What we built: `src/extract.py` with `read_json(path)`, plus a synthetic, deliberately messy `sample_data/patients.json`. Verified it reads 3 patient records into a list of dicts.
* What clicked / went well: clear on extract's single job and why isolation matters; mapped it to the page object and API client pattern from QA.
* What was hard / confusing: nothing; done under time pressure, so the tutor wrote the code and I reviewed it.
* Gate result: concept understood; explain back kept light due to time.
* Revisit later: none.
* Key takeaway: "Extraction is isolated on purpose: pull raw data into memory, so a source change touches only one step."
* Next step: 1.3, Transform clean.
