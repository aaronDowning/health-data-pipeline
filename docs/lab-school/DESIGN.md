---
title: Homelab Lab School — Learning System Design
status: approved-pending-review
created: 2026-06-01
type: design-spec
program: SYLLABUS.md
progress: PROGRESS.md
goal: An interactive, CLI-driven Socratic learning lab that teaches the Dell Med data-engineering stack so Aaron genuinely understands it (not just runs it), while producing a demoable healthcare data pipeline for the hiring team.
---

# Homelab Lab School — Design Spec

## Problem

The first-draft syllabus risked becoming a set of "run these commands" instructions for tools
Aaron has never used — producing a demo he couldn't *defend* when a technical panelist asks
"why does that work?" That's worse than not building it. We need a system where **understanding
is the unit of progress**, fully interactive from the CLI, that still yields a real demo.

## Design decisions (locked with Aaron)

1. **Engagement = Socratic live-tutor loop.** Claude teaches in the terminal, Aaron builds, and
   he doesn't advance until he can explain *why* it works.
2. **Sessions = short & resumable (30–45 min).** Each session opens with a recall quiz
   (spaced-repetition retrieval) before building anything new.
3. **Driven by a lightweight protocol doc.** No new tooling. Aaron says "let's do a lab session";
   Claude reads the syllabus + progress and follows `SESSION-PROTOCOL.md`. (May graduate into a
   `/lab` skill later if it earns it.)
4. **Hard gate + re-teach on failure.** If Aaron can't explain a concept back, we do not advance.
   Claude re-teaches it a different way (analogy / smaller example / break-it-and-watch-it-fail).
   Still stuck → log it, stop, resume the same lesson next session. No hollow knowledge.
5. **Selective typing (refined).** Aaron types the *thinking* code (transforms, SQL, DAGs, PySpark,
   data-quality checks). Claude scaffolds the *plumbing* (compose files, manifests, config). The
   hard gate applies to everything regardless of who typed it.

## System shape

Clean separation — **understanding lives in ai-os, the product lives in the repo:**

| Artifact | Location | Role |
|---|---|---|
| `SYLLABUS.md` | `documents/projects/dellmed-data-eng-homelab/` | Curriculum. Module-level, each module broken into ordered **mini-lessons** (concept + objective + explain-back question + "done when"). Lessons are NOT pre-written in full — the Socratic walk happens live. |
| `PROGRESS.md` | same folder | Learning state: **Current Position** pointer (resume cold, even mid-lesson), **Revisit Queue** (spaced-rep items), per-lesson retro entries. |
| `SESSION-PROTOCOL.md` | same folder | The engine — the exact loop Claude runs every session (below). |
| Code repo | separate GitHub repo `health-data-pipeline` | The artifact Aaron builds. CI runs here. Becomes the demo. |

Progress is measured by what Aaron can explain, not by what's been built.

## The session loop (`SESSION-PROTOCOL.md`)

```
0. RESUME    Claude reads SYLLABUS + PROGRESS, states exactly where we are.
1. RECALL    2-min retrieval quiz: last lesson + Revisit Queue items.
2. SCOPE     "How much time / how fried are you?" → size tonight's lesson.
3. TEACH     ONE concept, connected to what Aaron already knows
             (QA, CI/CD, Docker, homelab — never abstract).
4. BUILD     Aaron types the thinking code; Claude scaffolds plumbing and guides.
5. PREDICT   Before running: "what happens?" Aaron commits to an answer.
6. RUN       Run it. Prediction vs reality = the learning moment.
7. GATE      Explain-back TWO ways:
                a) to an engineer (precise/technical)
                b) to a non-technical stakeholder (plain English)
             ── HARD GATE ──
             Pass both → advance.
             Fail → re-teach differently → retry.
             Still stuck → log, STOP, resume this lesson next session. Do NOT advance.
8. LOG       Claude writes retro to PROGRESS + updates Current Position + Revisit Queue.
9. CHECKPOINT End clean so the next session resumes cold.
```

### Why the dual explain-back matters
The panel has technical AND non-technical people in the same room. Step 7 makes Aaron rehearse
explaining every concept both ways, every lesson. **The learning system doubles as panel prep.**

## Content rules

- **Selective typing:** thinking code by hand, plumbing scaffolded — gate applies to both.
- **Connect new → known:** Spark ↔ parallel test execution; Airflow ↔ CI pipeline DAGs;
  data-quality gates ↔ Push-on-Green. Attach new labels to models Aaron already owns.
- **Homelab → cloud mapping stays:** every tool tagged with its Fabric/Azure equivalent.
- **Break things on purpose** is a first-class teaching tool (QA instinct: learn systems by
  watching them fail).
- **The demo** = the Module 9 capstone (working FHIR pipeline), with a ready non-technical
  narration AND a technical deep-dive — the two audiences in the room.

## Scope (YAGNI)

In scope: learning the Dell Med stack + producing the capstone demo.
Out of scope: a general-purpose tutoring framework, a `/lab` skill (deferred), any cloud spend.

Build work required:
1. Write `SESSION-PROTOCOL.md` (the loop above, in runnable detail).
2. Re-chunk `SYLLABUS.md` modules into ordered mini-lessons with explain-back questions.
3. Extend `PROGRESS.md` with Current Position + Revisit Queue sections.

## Success criteria

- Aaron can run a 30-min session solo-initiated ("let's do a lab session") and it resumes cold.
- Every advanced lesson has a passed dual explain-back logged in PROGRESS.
- By the capstone, Aaron can demo the pipeline AND explain any layer to either audience.
- Net result: he can defend everything he built to a technical panelist.
