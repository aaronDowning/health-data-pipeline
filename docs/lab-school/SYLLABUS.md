---
title: Dell Med Data Engineer — Homelab Lab School (Syllabus)
status: active
created: 2026-06-01
updated: 2026-06-01
goal: Build real data-engineering skill (Spark, Airflow, warehousing, ETL) on the homelab via Socratic lab sessions, fill the gaps for the Dell Med / UT Austin role, and produce a demoable healthcare data pipeline for the hiring team.
design: DESIGN.md
protocol: SESSION-PROTOCOL.md
progress: PROGRESS.md
related_memory: project_dellmed_data_engineer
related_doc: documents/resume/interview-prep/dell-med-ut-austin-data-engineer-screening.md
---

# Homelab Lab School — Syllabus

A Socratic, CLI-driven learning lab. Each **module** breaks into ordered **mini-lessons**
(one concept each). We run them via `SESSION-PROTOCOL.md`: teach → you build → predict → run →
explain it two ways → log. **Understanding is the gate** — we don't advance past anything you
can't explain to both an engineer and a non-technical stakeholder.

The whole thing builds toward the **capstone**: an end-to-end, orchestrated, CI/CD-deployed
healthcare data pipeline on synthetic FHIR data — a working miniature of what this team does,
and the demo we show the hiring team.

## How to run it

- Say **"let's do a lab session"** → Claude follows `SESSION-PROTOCOL.md`.
- Sessions are short (30–45 min) and resume cold from the **Current Position** in `PROGRESS.md`.
- **Selective typing:** you type the *thinking* code (transforms, SQL, DAGs, PySpark, quality
  checks); Claude scaffolds the *plumbing* (compose, manifests, config). The gate applies to both.
- After every lesson, Claude logs a retro and updates the Revisit Queue.

## Stack (homelab → cloud mapping)

| Homelab tool (free, Docker) | Teaches | Microsoft Fabric / Azure equivalent |
|---|---|---|
| Python + pandas | ETL transform logic | Same |
| PostgreSQL | Relational warehouse, SQL depth | Azure SQL / Synapse Dedicated SQL Pool |
| MongoDB | NoSQL document store (raw FHIR bundles) | Azure Cosmos DB |
| Synthea + FHIR | Healthcare data, EHR formats | Same standards (Epic exports FHIR/HL7) |
| Apache Airflow | Orchestration / DAGs | Azure Data Factory / Fabric Data Pipelines |
| Apache Spark / PySpark | Distributed processing | Fabric Spark / Synapse Spark Pools |
| MinIO (S3-compatible) | Data lake / object storage | Azure Data Lake Storage / Fabric OneLake |
| dbt | SQL transforms + tests | Fabric notebooks / dataflows |
| Great Expectations | Data quality / validation | Fabric data quality + your QA instinct |
| GitHub Actions | CI/CD for pipelines | Azure DevOps Pipelines |
| Docker / docker-compose | Containerized deployment | Same |

> **Home field:** GitHub Actions + Docker are already your strengths — they're the backbone the
> whole program hangs on, so you start every module from confidence.

---

## Module 0 — Project setup & CI skeleton  *(home field — quick win)*

**Why:** Joshua specifically wants CI/CD + GitHub Actions. This module makes your pitch tangible
and sets the engineering hygiene that reads as senior.
**Repo:** create `health-data-pipeline` on GitHub (public, demoable).
**Capstone talking point:** "I scaffolded the repo with CI gating from commit one."

| # | Lesson | Objective | Explain-back focus | Done when |
|---|---|---|---|---|
| 0.1 | Repo & project structure | Lay out `src/ tests/ README` and why | Why separate src/tests; what a clean layout buys you | Structure exists, pushed |
| 0.2 | Dependencies & venv | Manage deps (uv/pip + venv) | What a virtualenv isolates and why it matters | Deps install reproducibly |
| 0.3 | First pytest | Write + run one passing test | What pytest asserts; why test-first here | `pytest` green locally |
| 0.4 | GitHub Actions: lint+test | CI runs on every push | Triggers/jobs/steps; why gate before merge | Green check on GitHub |
| 0.5 | docker-compose skeleton | Stand up empty compose on Rocky | What compose orchestrates; services/volumes/networks | `docker compose up` clean |

---

## Module 1 — Python ETL fundamentals

**Why:** The "can you code Python in an ETL" question Joshua hinted at. Maps to your Chartspan
HIPAA de-id work.
**Capstone talking point:** "I've built Python transforms that de-identify PHI and validate data quality."

| # | Lesson | Objective | Explain-back focus | Done when |
|---|---|---|---|---|
| 1.1 | The E/T/L model | Name the 3 stages + what lives where | What each stage does; where the logic concentrates | Can diagram E→T→L |
| 1.2 | Extract | Read a CSV/JSON source | Why isolate extract; handling source variance | Source reads into memory |
| 1.3 | Transform: clean | Dedupe, type-coerce, handle nulls | Why order matters; bad-data handling | Messy → clean rows |
| 1.4 | Transform: de-identify | Mask PHI (SSN, names) | What de-id is; why before load; HIPAA tie-in | PHI masked correctly |
| 1.5 | Load | Write to file/DB target | Idempotency; append vs replace | Output lands in target |
| 1.6 | Test + harden | Pytest the transform; add logging | Why test data logic; idempotency + logging | Edge-case tests green in CI |

---

## Module 2 — PostgreSQL warehouse + SQL depth

**Why:** The "L" + the data-warehousing requirement. SQL depth is a near-certain panel topic.
**Capstone talking point:** "I model the warehouse schema and can read an EXPLAIN plan."

| # | Lesson | Objective | Explain-back focus | Done when |
|---|---|---|---|---|
| 2.1 | Postgres in Docker | Run Postgres w/ a persistent volume | Why a volume; container vs data lifecycle | Can connect via psql |
| 2.2 | Schema modeling | Model patients/encounters/observations | Normalization vs star schema; keys | Tables created |
| 2.3 | Load via SQLAlchemy | Wire `load.py` to Postgres | Connection/session; why an ORM/engine | Data loaded from Module 1 |
| 2.4 | JOINs + CTEs | Query across tables, use CTEs | When a CTE clarifies; join types | Multi-table query returns |
| 2.5 | Window functions | Running totals / rankings | What a window does vs GROUP BY | Window query works + explained |
| 2.6 | EXPLAIN + indexes | Read a plan, add an index | What an index costs/buys; reading EXPLAIN | Index changes the plan |

---

## Module 3 — Synthetic healthcare data (Synthea + FHIR/HL7)

**Why:** The moat. Makes the project *healthcare*, ties to Epic, 100% HIPAA-safe (synthetic).
**Capstone talking point:** "I ingest synthetic FHIR and flatten it into a warehouse — same shape as an Epic FHIR export."

| # | Lesson | Objective | Explain-back focus | Done when |
|---|---|---|---|---|
| 3.1 | EHR / FHIR / HL7 / REDCap | Define the standards + capture tools | FHIR vs HL7 v2; Epic Clarity vs Caboodle; REDCap = research data capture (ubiquitous in academic med centers) | Can explain each in plain English |
| 3.2 | Run Synthea | Generate synthetic FHIR bundles | What a FHIR bundle/resource is | Bundles generated |
| 3.3 | Parse/flatten FHIR | Nested JSON → relational rows | Why flatten; resource → table mapping | Patient/Encounter rows extracted |
| 3.4 | Load FHIR → warehouse | Land parsed FHIR in Postgres | End-to-end ingest; Epic mapping | FHIR data queryable in warehouse |

---

## Module 3.5 — NoSQL document store (MongoDB)  *(required-quals gap-filler)*

**Why:** NoSQL is in the **Required Qualifications** ("experience with NoSQL databases is expected")
and the KSAs want schema design for *both* relational and NoSQL. Raw FHIR bundles are JSON
documents — so a document DB is their natural home, and this closes the one hard gap in the program.
**Capstone talking point:** "Raw FHIR lands in MongoDB as documents (bronze); I model the relational
warehouse in Postgres (silver/gold) — I've designed schemas for both paradigms."

> **Flow note:** this reroutes Module 3's ingest — FHIR now lands in **Mongo (raw/bronze)** first,
> then flattens into **Postgres (silver/gold)**. Cleaner medallion story than going straight to SQL.

| # | Lesson | Objective | Explain-back focus | Done when |
|---|---|---|---|---|
| 3.5.1 | Why NoSQL | Document vs relational; when each fits | Schema-on-read vs schema-on-write; why FHIR fits documents | Can explain the tradeoff both ways |
| 3.5.2 | MongoDB in Docker | Run Mongo w/ a persistent volume | Collections/documents vs tables/rows | Can connect + insert a doc |
| 3.5.3 | Land raw FHIR | Store Synthea bundles as documents (bronze) | Why keep raw as-is; document modeling | FHIR bundles queryable in Mongo |
| 3.5.4 | Query + index | Find/aggregate; add an index | Mongo query vs SQL; when to index | Aggregation returns + explained |

---

## Module 4 — Workflow orchestration with Airflow

**Why:** Explicit requirement. Maps to Azure Data Factory / Fabric pipelines.
**Capstone talking point:** "I orchestrated the pipeline as an Airflow DAG with retries and scheduling."

| # | Lesson | Objective | Explain-back focus | Done when |
|---|---|---|---|---|
| 4.1 | Why orchestrate | DAG concept vs cron | Why a DAG beats cron for dependencies | Can explain a DAG |
| 4.2 | Airflow anatomy | Run Airflow in Docker; tour UI | Scheduler/webserver/executor roles | Airflow UI up |
| 4.3 | First DAG | Tasks + dependencies | How deps define order; operators | DAG runs green |
| 4.4 | Schedule & retries | Scheduling, retries, backfill | Idempotency; why retries need it | Scheduled run + a forced retry |
| 4.5 | Pipeline as DAG | Wire generate→extract→transform→load→validate | The whole pipeline as one graph | Full DAG runs end to end |

---

## Module 5 — Distributed processing with Spark / PySpark

**Why:** Biggest listed gap. Closing it flips "haven't used Spark" → "I've written PySpark jobs."
**Capstone talking point:** "I've written PySpark transforms and can speak to optimizing them."

| # | Lesson | Objective | Explain-back focus | Done when |
|---|---|---|---|---|
| 5.1 | Why Spark | When Spark beats pandas | Distributed vs single-node; data > memory | Can explain the "kitchen of chefs" |
| 5.2 | Spark basics | Spark in Docker; DataFrames; lazy eval | What lazy evaluation buys | A Spark DataFrame op runs |
| 5.3 | PySpark transform | Rewrite Module 1 transform in PySpark | pandas → PySpark differences | Same transform, Spark version |
| 5.4 | Optimization | Partitioning, caching, shuffles | Why shuffles are costly; when to cache | Can name 3 optimization levers |

---

## Module 6 — Data lake + lakehouse (MinIO)

**Why:** "Structured and unstructured data," lakes, OneLake/ADLS concepts.
**Capstone talking point:** "I structured it as a medallion lakehouse — maps to OneLake + Synapse."

| # | Lesson | Objective | Explain-back focus | Done when |
|---|---|---|---|---|
| 6.1 | Lake vs warehouse vs lakehouse | Distinguish the three | Schema-on-read vs write; when each fits | Can explain all three |
| 6.2 | MinIO in Docker | Object storage; land raw bundles (bronze) | What object storage is vs a DB | Raw FHIR in MinIO |
| 6.3 | Medallion layers | bronze → silver → gold flow | Why layered refinement | Data flows lake → warehouse |

---

## Module 7 — Data quality & testing  *(your superpower, applied to data)*

**Why:** "Validates data for accuracy and consistency" is literally your career. 23 years of QA
becomes a data-engineering differentiator here.
**Capstone talking point:** "I treat data quality like test quality — automated gates that fail the pipeline loudly."

| # | Lesson | Objective | Explain-back focus | Done when |
|---|---|---|---|---|
| 7.1 | Data contracts | Expectations/assertions concept | Data quality vs test quality parallel | Can explain a data contract |
| 7.2 | Great Expectations | Set up GE (or dbt tests) | What an expectation suite is | GE runs against the data |
| 7.3 | Key checks | Nulls, ranges, PHI-masked, referential | Which checks catch which failures | Checks pass on good data |
| 7.4 | Quality gate in DAG | Fail the run on a bad record | Why fail loud > silent corruption | Bad record fails the pipeline |

---

## Module 7.5 — Analytics dashboard  *(optional — maps to a JD responsibility)*

**Why:** The JD calls for "analytics tools that empower analysts" and "data visualizations for
non-technical stakeholders." A light dashboard on the gold layer makes that tangible. Optional
polish, not a gap.
**Capstone talking point:** "The gold layer feeds a dashboard — quality/outcome reporting for non-technical users."

| # | Lesson | Objective | Explain-back focus | Done when |
|---|---|---|---|---|
| 7.5.1 | Dashboard on gold | Stand up Metabase (or Streamlit) on the warehouse | Why gold feeds BI; analyst self-serve | A chart renders from gold data |
| 7.5.2 | An outcome report | Build one quality/outcome view | What makes a report stakeholder-ready | A non-technical user could read it |

---

## Module 8 — CI/CD for the whole pipeline  *(home field finale)*

**Why:** Ties the bow on the CI/CD strength Joshua wants, applied to data infra.
**Capstone talking point:** "The whole platform deploys on push — Push-on-Green for data infra."

| # | Lesson | Objective | Explain-back focus | Done when |
|---|---|---|---|---|
| 8.1 | CI vs CD | Define the deploy target | Where CI ends and CD begins | Can explain both |
| 8.2 | Build & push images | GHA builds Docker images | Why containerize the deploy | Images build in CI |
| 8.3 | Deploy to Rocky | Self-hosted runner / SSH deploy | Deploy strategy; secrets handling | Push refreshes the stack |
| 8.4 | Smoke test + protection | Trigger DAG post-deploy; branch rules | Why smoke-test; required checks | Push → deploy → verified run |

---

## Module 9 — Capstone & demo for the hiring team

**Why:** Turn it into a clean demo and writeup. The standout move.

| # | Lesson | Objective | Explain-back focus | Done when |
|---|---|---|---|---|
| 9.1 | README + diagram | Architecture diagram + homelab→cloud map | The whole system in one picture | README reads clean |
| 9.2 | Technical demo | <10-min walkthrough for engineers | Every layer, deeply | Can demo end to end |
| 9.3 | Stakeholder narration | Plain-English version | The "so what" with no jargon | Non-technical version ready |
| 9.4 | Dry run | Full rehearsal of the demo | Handle a curveball question | Demo runs flawlessly once |

**The standout line for the panel:** "I'm already building this in my homelab — want to see it?"
Almost nobody shows up having built a working miniature of the employer's actual platform.

---

## Appendix — Cloud concepts to read (can't homelab, must speak to)

- **Microsoft Fabric:** OneLake (storage), Data Factory (pipelines), Synapse (warehouse + Spark),
  notebooks. Likely their stack given Epic + Microsoft.
- **Azure Data Factory:** managed orchestration (cloud Airflow).
- **Azure Synapse:** cloud warehouse + managed Spark.
- **Certs (preferred quals):** Azure Data Engineer Associate (mention you'd pursue this),
  GCP Professional Data Engineer, AWS Data Analytics Specialty.

## Reality check on pacing

Friday's panel needs **none** of this built — conversational fluency (see the prep doc) wins it.
This program is the **60-day-ramp play** + a hard-to-refuse demo. Standing up just **Module 0**
before Friday earns the line: "I'm already building a FHIR pipeline with CI/CD in my homelab."
