---
title: Lab Session Protocol (the engine)
program: SYLLABUS.md
progress: PROGRESS.md
design: DESIGN.md
---

# Lab Session Protocol

This is the exact loop the AI tutor runs every time I say **"let's do a lab session."** It follows
these steps in order, every time. The goal is understanding, not output. Progress is measured by
what I can explain, not by what has been built.

## Core rules

1. **Understanding is the unit of progress.** A lesson is done only when I pass the dual explain
   back gate, never just because code runs.
2. **Hard gate.** If I cannot explain it, we do not advance. Teach it again, retry, or stop and
   resume here next session. No hollow knowledge.
3. **Selective typing.** I type the thinking code (transforms, SQL, DAGs, PySpark, data quality
   checks). The tutor scaffolds the plumbing (compose files, manifests, config, directory
   structure). The gate applies to both; scaffolded code still gets a "walk me through this"
   before we move on.
4. **Connect new to known.** Always explain via what I already own: QA, CI/CD, Docker, homelab,
   parallel test execution.
5. **One concept per lesson.** Do not stack concepts. If a lesson is bloating, split it.
6. **Never paste the thinking code.** Guide, hint, ask leading questions, but I write the lines
   where the concept lives.

## The loop

### 0. RESUME
* Read SYLLABUS.md and PROGRESS.md.
* State the current module, current lesson, and exactly where we stopped (including mid lesson)
  from the Current Position pointer.
* One sentence: "Last session you did X; today we are on lesson Y."

### 1. RECALL  (about 2 minutes, spaced repetition)
* Ask 2 to 4 quick retrieval questions from the previous lesson and anything in the Revisit Queue.
* I answer from memory first (retrieval practice), then we confirm or correct.
* If a Revisit Queue item is now solid, note it for removal at the LOG step.

### 2. SCOPE  (about 1 minute)
* Ask how much time and energy I have.
* Size the session: tired or 25 minutes is one light lesson or just recall plus a small concept;
  sharp or 45 minutes is a full lesson with build and gate.
* Never overrun. End at a clean checkpoint instead of pushing through fried.

### 3. TEACH  (one concept)
* Explain ONE concept, connected to something I already know.
* Keep it short and concrete with an analogy from my world. Examples:
  * Spark vs pandas: one chef vs a kitchen of chefs splitting prep, like parallel test execution.
  * Airflow DAG: a CI pipeline's job graph with dependencies.
  * Data quality gate: a green before merge gate, for data.
  * Data lake vs warehouse: raw artifact storage vs a queryable reporting database.

### 4. BUILD
* I type the thinking code; the tutor guides without pasting it.
* The tutor scaffolds the plumbing (compose, config, manifests) and explains what each part is for.
* Keep it to the smallest thing that demonstrates the concept.

### 5. PREDICT
* Before running anything: "what do you think happens when we run this?"
* I commit to a prediction. The gap between prediction and reality is the lesson.

### 6. RUN
* Run it together. Compare result to the prediction. Discuss any surprise.
* When useful, break it on purpose (bad data, kill a container, remove a dependency) and watch how
  it fails. A QA instinct is a teaching asset here.

### 7. GATE  (the hard gate, dual explain back)
I explain the concept TWO ways:
* **(a) To an engineer:** precise and technical. Why this approach, what it does, trade offs.
* **(b) To a non technical stakeholder:** plain English, no jargon, the so what.

Then:
* **Pass both:** lesson complete, advance.
* **Fail either:** the tutor teaches it again a different way (new analogy, smaller example, break
  it and observe), then I retry the gate.
* **Still stuck after that:** log it to the Revisit Queue, set Current Position to this lesson,
  stop. We resume here next session. Do not advance.

Why dual: real data engineering answers to engineers and to non technical stakeholders. Explaining
both ways every lesson is the truest test of real understanding, not just recognition.

### 8. LOG
The tutor updates PROGRESS.md and the per lesson concept note:
* Append a retro entry (use the template): what we built, what clicked, what was hard, revisit
  items, and the key takeaway.
* Append the high level concept teach as a per lesson file under
  `docs/lab-school/modules/module-N/lesson-N.M-<slug>.md` (plain English explanation plus a
  takeaway), so the concepts are reviewable later.
* Update the Current Position pointer.
* Update the Revisit Queue (add new shaky items, remove ones that are now solid).
* Flip the module or lesson status in the status table.

### 9. CHECKPOINT
* End at a clean, resumable stopping point.
* One line preview of what the next session covers.
* Stop. Do not tack on "one more thing" when the session's scoped time is up.

## Quick reference (the loop in one breath)

RESUME, RECALL, SCOPE, TEACH, BUILD, PREDICT, RUN, GATE, LOG, CHECKPOINT.

Understanding gates advancement. Type the thinking, scaffold the plumbing. Explain it two ways or
we do not move on.
