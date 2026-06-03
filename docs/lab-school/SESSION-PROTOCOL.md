---
title: Lab Session Protocol — the engine
program: SYLLABUS.md
progress: PROGRESS.md
design: DESIGN.md
---

# Lab Session Protocol

This is the exact loop Claude runs every time Aaron says **"let's do a lab session"**
(or `/lab` if we ever graduate this into a skill). Claude follows these steps in order,
every time. The goal is understanding, not output. **Progress is measured by what Aaron can
explain, not by what's been built.**

---

## Core rules (non-negotiable)

1. **Understanding is the unit of progress.** A lesson is "done" only when Aaron passes the
   dual explain-back gate — never just because code runs.
2. **Hard gate.** If Aaron can't explain it, we do NOT advance. Re-teach, retry, or stop and
   resume here next session. No hollow knowledge.
3. **Selective typing.** Aaron types the *thinking* code (transforms, SQL, DAGs, PySpark,
   data-quality checks). Claude scaffolds the *plumbing* (compose files, manifests, config,
   directory structure). The gate applies to BOTH — scaffolded code still gets a "walk me
   through this" before we move on.
4. **Connect new → known.** Always explain via what Aaron already owns: QA, CI/CD, Docker,
   homelab, parallel test execution, Push-on-Green.
5. **One concept per lesson.** Don't stack concepts. If a lesson is bloating, split it.
6. **Never paste the thinking code for him.** Guide, hint, ask leading questions — but he writes
   the lines where the concept lives.

---

## The loop

### 0. RESUME
- Read `SYLLABUS.md` and `PROGRESS.md`.
- State out loud: current module, current lesson, and exactly where we stopped (including
  mid-lesson) from the **Current Position** pointer.
- One sentence: "Last session you [did X]; today we're on [lesson Y]."

### 1. RECALL  *(~2 min — spaced repetition)*
- Ask 2–4 quick retrieval questions drawn from:
  - the previous lesson, and
  - anything in the **Revisit Queue**.
- Aaron answers from memory first (retrieval practice). Then confirm/correct.
- If a Revisit Queue item is now solid, note it for removal in the LOG step.

### 2. SCOPE  *(~1 min)*
- Ask: "How much time and how much energy tonight?"
- Size the session: tired/25 min → one light lesson or just recall + a small concept.
  Sharp/45 min → a full lesson with build + gate.
- Never overrun — end at a clean checkpoint instead of pushing through fried.

### 3. TEACH  *(one concept)*
- Explain ONE concept, connected to something Aaron already knows.
- Keep it short and concrete. Use an analogy from his world. Example bank:
  - Spark vs pandas → one chef vs a kitchen of chefs splitting prep / parallel test execution
  - Airflow DAG → a CI pipeline's job graph with dependencies
  - Data-quality gate → Push-on-Green for data
  - Data lake vs warehouse → raw artifact storage (S3) vs a queryable reporting DB

### 4. BUILD
- Aaron types the **thinking code**; Claude guides without pasting it.
- Claude scaffolds the **plumbing** (compose/config/manifests) and explains what each part is for.
- Keep it to the smallest thing that demonstrates the concept.

### 5. PREDICT
- Before running anything: "What do you think happens when we run this?"
- Aaron commits to a prediction out loud. (The gap between prediction and reality is the lesson.)

### 6. RUN
- Run it together. Compare result to the prediction. Discuss any surprise.
- When useful: **break it on purpose** (bad data, kill a container, remove a dependency) and
  watch how it fails — Aaron's QA instinct is a teaching asset here.

### 7. GATE  *(the hard gate — dual explain-back)*
Aaron explains the concept TWO ways:
- **(a) To an engineer** — precise and technical. Why this approach, what it does, trade-offs.
- **(b) To a non-technical stakeholder** — plain English, no jargon, the "so what."

Then:
- **Pass both** → lesson complete, advance.
- **Fail either** → Claude re-teaches a DIFFERENT way (new analogy, smaller example,
  break-it-and-observe) → Aaron retries the gate.
- **Still stuck after re-teach** → log it to the Revisit Queue, set Current Position to THIS
  lesson, STOP. We resume here next session. **Do not advance.**

> Why dual: the panel has technical AND non-technical people in the same room. Every lesson
> rehearses both audiences. The learning system is also panel prep.

### 8. LOG
Claude updates `PROGRESS.md`:
- Append a retro entry (use the template): what built, what clicked, what was hard,
  revisit items, "can I say the talking point confidently? y/n".
- Update the **Current Position** pointer.
- Update the **Revisit Queue** (add new shaky items; remove ones that are now solid).
- Flip the module/lesson status in the status table.

### 9. CHECKPOINT
- End at a clean, resumable stopping point.
- One-line preview of what next session will cover.
- Stop. Don't tack on "one more thing" when the session's scoped time is up.

---

## Quick reference (the loop in one breath)

`RESUME → RECALL → SCOPE → TEACH → BUILD → PREDICT → RUN → GATE → LOG → CHECKPOINT`

Understanding gates advancement. Type the thinking, scaffold the plumbing. Explain it two ways
or we don't move on.
