# health-data-pipeline

An end-to-end, orchestrated, CI/CD-deployed healthcare data pipeline built on synthetic
FHIR data — a working miniature of a modern health-data platform.

## What this is
A learning + demo project: ingest synthetic FHIR (Synthea) → land raw in a document store →
clean and model into a SQL warehouse → orchestrate with Airflow → validate with automated
data-quality gates → deploy via GitHub Actions. Built in a homelab, mapped to Microsoft Fabric / Azure.

## Structure
- `src/` — the pipeline code (extract, transform, load, quality checks)
- `tests/` — automated tests that prove `src/` behaves; gate every change in CI
- `README.md` — you are here

## Status
🚧 In progress — Module 0: project setup & CI skeleton.
