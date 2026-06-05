# health-data-pipeline

An end to end, orchestrated, CI/CD deployed healthcare data pipeline built on synthetic FHIR data.

## What this is
This project ingests synthetic FHIR data (Synthea), lands it raw in a document store, cleans and
models it into a SQL warehouse, orchestrates it with Airflow, validates it with automated data
quality gates, and deploys it through GitHub Actions. It is built in a homelab and mapped, tool for
tool, to Microsoft Fabric and Azure equivalents.

## How it was built
This repo is also a learning system. Rather than follow tutorials passively, I built an AI native,
Socratic lab school: a structured curriculum run as short, understanding gated sessions, where a
lesson only counts as done when I can explain it two ways, to an engineer and to a non technical
stakeholder. The curriculum, the session protocol, per lesson concept notes, and a running progress
log all live in `docs/lab-school/`.

## Structure
* `src/` the pipeline code (extract, transform, load, quality checks)
* `tests/` automated tests that prove `src/` behaves; they gate every change in CI
* `docs/lab-school/` the curriculum, learning protocol, concept notes, and progress log
* `README.md` you are here

## Status
In progress. Module 0 (project setup and CI skeleton) is underway. See
`docs/lab-school/PROGRESS.md` for the live status.
