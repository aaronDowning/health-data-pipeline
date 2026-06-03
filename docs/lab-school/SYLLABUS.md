---
title: Healthcare Data Engineering — Lab School Syllabus
status: active
created: 2026-06-01
design: DESIGN.md
protocol: SESSION-PROTOCOL.md
progress: PROGRESS.md
---

# Lab School Syllabus

A Socratic, CLI driven, AI native learning lab. Each **module** breaks into ordered
**mini lessons** (one concept each). They run via `SESSION-PROTOCOL.md`: teach, I build, predict,
run, explain it two ways, log. **Understanding is the gate.** Nothing advances past anything I
cannot explain to both an engineer and a non technical stakeholder.

The whole thing builds toward the **capstone**: an end to end, orchestrated, CI/CD deployed
healthcare data pipeline on synthetic FHIR data. A working miniature of a real health data
platform, and the demo for the project.

## How to run it

* Say **"let's do a lab session"** and the AI tutor follows `SESSION-PROTOCOL.md`.
* Sessions are short (30 to 45 minutes) and resume cold from the **Current Position** in `PROGRESS.md`.
* **Selective typing:** I type the *thinking* code (transforms, SQL, DAGs, PySpark, quality
  checks); the tutor scaffolds the *plumbing* (compose, manifests, config). The gate applies to both.
* After every lesson, the tutor logs a retro and updates the Revisit Queue.

## Stack (homelab to cloud mapping)

| Homelab tool (free, Docker) | Teaches | Microsoft Fabric / Azure equivalent |
|---|---|---|
| Python + pandas | ETL transform logic | Same |
| PostgreSQL | Relational warehouse, SQL depth | Azure SQL / Synapse Dedicated SQL Pool |
| MongoDB | NoSQL document store (raw FHIR bundles) | Azure Cosmos DB |
| Synthea + FHIR | Healthcare data, EHR formats | Same standards (Epic exports FHIR/HL7) |
| Apache Airflow | Orchestration / DAGs | Azure Data Factory / Fabric Data Pipelines |
| Apache Spark / PySpark | Distributed processing | Fabric Spark / Synapse Spark Pools |
| MinIO (S3 compatible) | Data lake / object storage | Azure Data Lake Storage / Fabric OneLake |
| dbt | SQL transforms + tests | Fabric notebooks / dataflows |
| Great Expectations | Data quality / validation | Fabric data quality checks |
| GitHub Actions | CI/CD for pipelines | Azure DevOps Pipelines |
| Docker / docker-compose | Containerized deployment | Same |

> **Home field:** GitHub Actions and Docker are already my strengths, so they are the backbone the
> whole program hangs on. Every module starts from a base of confidence.

## Module 0: Project setup and CI skeleton  *(home field, quick win)*

**Why:** Clean engineering hygiene and CI from the first commit is the backbone everything else
hangs on. Starting on home field (CI/CD, Docker) sets the standard for the whole project.
**Repo:** the `health-data-pipeline` repo, demoable.
**What it demonstrates:** "I scaffolded the repo with CI gating from commit one."

| # | Lesson | Objective | Explain back focus | Done when |
|---|---|---|---|---|
| 0.1 | Repo and project structure | Lay out `src/ tests/ README` and why | Why separate src and tests; what a clean layout buys | Structure exists, pushed |
| 0.2 | Dependencies and venv | Manage deps (pip + venv) | What a virtualenv isolates and why it matters | Deps install reproducibly |
| 0.3 | First pytest | Write and run one passing test | What pytest asserts; why test first here | `pytest` green locally |
| 0.4 | GitHub Actions: lint + test | CI runs on every push | Triggers, jobs, steps; why gate before merge | Green check on GitHub |
| 0.5 | docker-compose skeleton | Stand up an empty compose on the homelab host | What compose orchestrates; services, volumes, networks | `docker compose up` clean |

## Module 1: Python ETL fundamentals

**Why:** ETL is the core of data engineering. Maps to my HIPAA de identification experience.
**What it demonstrates:** "I build Python transforms that de identify PHI and validate data quality."

| # | Lesson | Objective | Explain back focus | Done when |
|---|---|---|---|---|
| 1.1 | The E/T/L model | Name the 3 stages and what lives where | What each stage does; where the logic concentrates | Can diagram E to T to L |
| 1.2 | Extract | Read a CSV or JSON source | Why isolate extract; handling source variance | Source reads into memory |
| 1.3 | Transform: clean | Dedupe, coerce types, handle nulls | Why order matters; bad data handling | Messy rows become clean |
| 1.4 | Transform: de identify | Mask PHI (SSN, names) | What de identification is; why before load; HIPAA tie in | PHI masked correctly |
| 1.5 | Load | Write to a file or DB target | Idempotency; append vs replace | Output lands in target |
| 1.6 | Test and harden | Pytest the transform; add logging | Why test data logic; idempotency and logging | Edge case tests green in CI |

## Module 2: PostgreSQL warehouse and SQL depth

**Why:** The load stage and the data warehousing core. SQL depth is foundational.
**What it demonstrates:** "I model the warehouse schema and can read an EXPLAIN plan."

| # | Lesson | Objective | Explain back focus | Done when |
|---|---|---|---|---|
| 2.1 | Postgres in Docker | Run Postgres with a persistent volume | Why a volume; container vs data lifecycle | Can connect via psql |
| 2.2 | Schema modeling | Model patients, encounters, observations | Normalization vs star schema; keys | Tables created |
| 2.3 | Load via SQLAlchemy | Wire `load.py` to Postgres | Connection and session; why an engine | Data loaded from Module 1 |
| 2.4 | JOINs and CTEs | Query across tables, use CTEs | When a CTE clarifies; join types | Multi table query returns |
| 2.5 | Window functions | Running totals and rankings | What a window does vs GROUP BY | Window query works and explained |
| 2.6 | EXPLAIN and indexes | Read a plan, add an index | What an index costs and buys; reading EXPLAIN | Index changes the plan |

## Module 3: Synthetic healthcare data (Synthea + FHIR/HL7)

**Why:** Makes the project genuinely healthcare, ties to Epic data shapes, and is fully HIPAA safe
because the data is synthetic.
**What it demonstrates:** "I ingest synthetic FHIR and flatten it into a warehouse, the same shape as an Epic FHIR export."

| # | Lesson | Objective | Explain back focus | Done when |
|---|---|---|---|---|
| 3.1 | EHR / FHIR / HL7 / REDCap | Define the standards and capture tools | FHIR vs HL7 v2; Epic Clarity vs Caboodle; REDCap is research data capture, common in academic medical centers | Can explain each in plain English |
| 3.2 | Run Synthea | Generate synthetic FHIR bundles | What a FHIR bundle and resource are | Bundles generated |
| 3.3 | Parse and flatten FHIR | Nested JSON into relational rows | Why flatten; resource to table mapping | Patient and Encounter rows extracted |
| 3.4 | Load FHIR to warehouse | Land parsed FHIR in Postgres | End to end ingest; Epic mapping | FHIR data queryable in warehouse |

## Module 3.5: NoSQL document store (MongoDB)

**Why:** Real data engineering uses both relational and NoSQL, and schema design differs for each.
Raw FHIR bundles are JSON documents, so a document database is their natural home.
**What it demonstrates:** "Raw FHIR lands in MongoDB as documents (bronze); I model the relational warehouse in Postgres (silver and gold). I have designed schemas for both paradigms."

> **Flow note:** this reroutes Module 3's ingest. FHIR now lands in **Mongo (raw, bronze)** first,
> then flattens into **Postgres (silver, gold)**. A cleaner medallion story than going straight to SQL.

| # | Lesson | Objective | Explain back focus | Done when |
|---|---|---|---|---|
| 3.5.1 | Why NoSQL | Document vs relational; when each fits | Schema on read vs schema on write; why FHIR fits documents | Can explain the tradeoff both ways |
| 3.5.2 | MongoDB in Docker | Run Mongo with a persistent volume | Collections and documents vs tables and rows | Can connect and insert a doc |
| 3.5.3 | Land raw FHIR | Store Synthea bundles as documents (bronze) | Why keep raw as is; document modeling | FHIR bundles queryable in Mongo |
| 3.5.4 | Query and index | Find, aggregate, add an index | Mongo query vs SQL; when to index | Aggregation returns and explained |

## Module 4: Workflow orchestration with Airflow

**Why:** Orchestration is a core data engineering skill. Maps to Azure Data Factory and Fabric pipelines.
**What it demonstrates:** "I orchestrated the pipeline as an Airflow DAG with retries and scheduling."

| # | Lesson | Objective | Explain back focus | Done when |
|---|---|---|---|---|
| 4.1 | Why orchestrate | DAG concept vs cron | Why a DAG beats cron for dependencies | Can explain a DAG |
| 4.2 | Airflow anatomy | Run Airflow in Docker; tour the UI | Scheduler, webserver, executor roles | Airflow UI up |
| 4.3 | First DAG | Tasks and dependencies | How deps define order; operators | DAG runs green |
| 4.4 | Schedule and retries | Scheduling, retries, backfill | Idempotency; why retries need it | Scheduled run plus a forced retry |
| 4.5 | Pipeline as DAG | Wire generate, extract, transform, load, validate | The whole pipeline as one graph | Full DAG runs end to end |

## Module 5: Distributed processing with Spark / PySpark

**Why:** Distributed processing of large datasets is a core skill, and the most valuable gap to close.
**What it demonstrates:** "I have written PySpark transforms and can speak to optimizing them."

| # | Lesson | Objective | Explain back focus | Done when |
|---|---|---|---|---|
| 5.1 | Why Spark | When Spark beats pandas | Distributed vs single node; data larger than memory | Can explain the kitchen of chefs |
| 5.2 | Spark basics | Spark in Docker; DataFrames; lazy eval | What lazy evaluation buys | A Spark DataFrame op runs |
| 5.3 | PySpark transform | Rewrite the Module 1 transform in PySpark | pandas vs PySpark differences | Same transform, Spark version |
| 5.4 | Optimization | Partitioning, caching, shuffles | Why shuffles are costly; when to cache | Can name 3 optimization levers |

## Module 6: Data lake and lakehouse (MinIO)

**Why:** Structured and unstructured data, lakes, and the OneLake and ADLS concepts.
**What it demonstrates:** "I structured it as a medallion lakehouse, which maps to OneLake plus Synapse."

| # | Lesson | Objective | Explain back focus | Done when |
|---|---|---|---|---|
| 6.1 | Lake vs warehouse vs lakehouse | Distinguish the three | Schema on read vs write; when each fits | Can explain all three |
| 6.2 | MinIO in Docker | Object storage; land raw bundles (bronze) | What object storage is vs a DB | Raw FHIR in MinIO |
| 6.3 | Medallion layers | bronze, silver, gold flow | Why layered refinement | Data flows lake to warehouse |

## Module 7: Data quality and testing  *(my superpower, applied to data)*

**Why:** Validating data for accuracy and consistency is the heart of my QA background. Years of QA
become a data engineering differentiator here.
**What it demonstrates:** "I treat data quality like test quality: automated gates that fail the pipeline loudly."

| # | Lesson | Objective | Explain back focus | Done when |
|---|---|---|---|---|
| 7.1 | Data contracts | Expectations and assertions concept | Data quality vs test quality parallel | Can explain a data contract |
| 7.2 | Great Expectations | Set up GE (or dbt tests) | What an expectation suite is | GE runs against the data |
| 7.3 | Key checks | Nulls, ranges, PHI masked, referential | Which checks catch which failures | Checks pass on good data |
| 7.4 | Quality gate in DAG | Fail the run on a bad record | Why fail loud beats silent corruption | Bad record fails the pipeline |

## Module 7.5: Analytics dashboard  *(optional)*

**Why:** Analytics tools that empower analysts, and data visualizations for non technical
stakeholders, are a common data engineering responsibility. A light dashboard on the gold layer
makes that tangible.
**What it demonstrates:** "The gold layer feeds a dashboard: quality and outcome reporting for non technical users."

| # | Lesson | Objective | Explain back focus | Done when |
|---|---|---|---|---|
| 7.5.1 | Dashboard on gold | Stand up Metabase (or Streamlit) on the warehouse | Why gold feeds BI; analyst self serve | A chart renders from gold data |
| 7.5.2 | An outcome report | Build one quality or outcome view | What makes a report stakeholder ready | A non technical user could read it |

## Module 8: CI/CD for the whole pipeline  *(home field finale)*

**Why:** Applies the CI/CD strength to data infrastructure, end to end.
**What it demonstrates:** "The whole platform deploys on push: deploy on green, for data infrastructure."

| # | Lesson | Objective | Explain back focus | Done when |
|---|---|---|---|---|
| 8.1 | CI vs CD | Define the deploy target | Where CI ends and CD begins | Can explain both |
| 8.2 | Build and push images | GHA builds Docker images | Why containerize the deploy | Images build in CI |
| 8.3 | Deploy to the homelab | Self hosted runner or SSH deploy | Deploy strategy; secrets handling | Push refreshes the stack |
| 8.4 | Smoke test and protection | Trigger the DAG after deploy; branch rules | Why smoke test; required checks | Push, deploy, verified run |

## Module 9: Capstone and demo

**Why:** Turn the pipeline into a clean demo and writeup. The standout move is a working miniature
of a real health data platform, end to end, that I can explain at any layer.

| # | Lesson | Objective | Explain back focus | Done when |
|---|---|---|---|---|
| 9.1 | README and diagram | Architecture diagram plus the homelab to cloud map | The whole system in one picture | README reads clean |
| 9.2 | Technical demo | A walkthrough for engineers, under 10 minutes | Every layer, deeply | Can demo end to end |
| 9.3 | Stakeholder narration | The plain English version | The so what, with no jargon | Non technical version ready |
| 9.4 | Dry run | Full rehearsal of the demo | Handle a curveball question | Demo runs cleanly once |

## Appendix: cloud concepts worth understanding

These cannot be run on a homelab, but they are worth being able to speak to. The homelab tools above
each map to one of them.

* **Microsoft Fabric:** OneLake (storage), Data Factory (pipelines), Synapse (warehouse plus Spark),
  notebooks. A common modern healthcare data platform, especially in Microsoft and Epic shops.
* **Azure Data Factory:** managed orchestration, the cloud equivalent of Airflow.
* **Azure Synapse:** cloud warehouse plus managed Spark.
* **Relevant certifications:** Azure Data Engineer Associate, Google Cloud Professional Data
  Engineer, AWS Data Analytics Specialty.

## Pacing

This is a deliberate, paced program, and each module stands on its own. Even Module 0 alone produces
a working repo with CI gating from the first commit. The homelab to cloud mapping means everything
built here transfers directly to a Microsoft Fabric or Azure data platform.
