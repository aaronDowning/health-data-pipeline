---
title: Lab School — Learning System Design
status: active
created: 2026-06-01
type: design-spec
program: SYLLABUS.md
progress: PROGRESS.md
goal: An interactive, CLI driven, AI native Socratic learning lab that teaches a modern healthcare data engineering stack so I genuinely understand it (not just run it), while producing a real, demoable healthcare data pipeline.
---

# Lab School: Design Spec

## Problem
A first draft syllabus risks becoming a set of "run these commands" instructions for tools I have
not used, producing a project I could not defend when someone asks "why does that work?". That is
worse than not building it. I wanted a system where understanding is the unit of progress, fully
interactive from the CLI, that still yields a real, working artifact.

## Design decisions
1. Engagement is a Socratic live tutor loop. An AI tutor teaches in the terminal, I build, and I do
   not advance until I can explain why it works.
2. Sessions are short and resumable (30 to 45 minutes). Each session opens with a recall quiz
   (spaced repetition retrieval) before building anything new.
3. Driven by a lightweight protocol doc, no new tooling. I say "let's do a lab session"; the tutor
   reads the syllabus and progress and follows SESSION-PROTOCOL.md.
4. Hard gate and reteach on failure. If I cannot explain a concept back, we do not advance. The
   tutor teaches it again a different way (analogy, smaller example, break it and watch it fail).
   Still stuck, we log it, stop, and resume the same lesson next session. No hollow knowledge.
5. Selective typing. I type the thinking code (transforms, SQL, DAGs, PySpark, data quality checks).
   The tutor scaffolds the plumbing (compose files, manifests, config). The hard gate applies to
   everything regardless of who typed it.

## System shape
The learning lives next to the code it produces.

| Artifact | Location | Role |
|---|---|---|
| SYLLABUS.md | docs/lab-school/ | Curriculum. Module level, each module broken into ordered mini lessons (concept, objective, explain back question, "done when"). Lessons are not pre written in full; the Socratic walk happens live. |
| PROGRESS.md | docs/lab-school/ | Learning state: a Current Position pointer (resume cold, even mid lesson), a Revisit Queue (spaced repetition items), and per lesson retro entries. |
| SESSION-PROTOCOL.md | docs/lab-school/ | The engine: the exact loop the tutor runs every session (below). |
| modules/ | docs/lab-school/modules/ | A plain English concept note per lesson, for review. |
| Code | repo root (src/, tests/) | The artifact I build. CI runs here. Becomes the demo. |

Progress is measured by what I can explain, not by what has been built.

## The session loop (SESSION-PROTOCOL.md)
```
0. RESUME    Read SYLLABUS + PROGRESS, state exactly where we are.
1. RECALL    2 min retrieval quiz: last lesson + Revisit Queue items.
2. SCOPE     "How much time and energy?" then size the lesson.
3. TEACH     ONE concept, connected to something I already know
             (QA, CI/CD, Docker, homelab), never abstract.
4. BUILD     I type the thinking code; the tutor scaffolds plumbing and guides.
5. PREDICT   Before running: "what happens?" I commit to an answer.
6. RUN       Run it. Prediction vs reality is the learning moment.
7. GATE      Explain back TWO ways:
                a) to an engineer (precise, technical)
                b) to a non technical stakeholder (plain English)
             Hard gate. Pass both, advance. Fail, teach it again, retry.
             Still stuck, log, stop, resume next session. Do not advance.
8. LOG       Write a retro to PROGRESS, update Current Position and Revisit Queue,
             and save the concept note.
9. CHECKPOINT End clean so the next session resumes cold.
```

### Why the dual explain back matters
Real data engineering answers to two audiences: engineers who want the technical why, and
stakeholders who want the plain English so what. Step 7 makes me rehearse both for every concept,
which is the truest test that I actually understand it rather than just recognize it.

## Content rules
* Selective typing: thinking code by hand, plumbing scaffolded, gate applies to both.
* Connect new to known: Spark and parallel test execution; Airflow and CI pipeline DAGs; data
  quality gates and a green before merge gate. Attach new labels to models I already own.
* Homelab to cloud mapping stays: every tool tagged with its Microsoft Fabric or Azure equivalent.
* Break things on purpose is a first class teaching tool (a QA instinct: learn systems by watching
  them fail).
* The demo is the Module 9 capstone (a working FHIR pipeline), with a ready plain English narration
  and a technical deep dive, for both audiences.

## Scope
In scope: learning the stack and producing the capstone demo.
Out of scope: a general purpose tutoring framework, any cloud spend.

## Success criteria
* I can run a 30 minute session, self started ("let's do a lab session"), and it resumes cold.
* Every advanced lesson has a passed dual explain back logged in PROGRESS.
* By the capstone, I can demo the pipeline and explain any layer to either audience.
