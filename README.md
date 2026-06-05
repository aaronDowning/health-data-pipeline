# health-data-pipeline

A healthcare data pipeline built on synthetic FHIR shaped data, with a full learning curriculum covering the complete modern data engineering stack.

## What this is
This project extracts synthetic patient records, cleans and de identifies them, and loads the results
through a tested, idempotent ETL pipeline deployed with GitHub Actions CI. It is built in Python with
pytest, a Makefile, and a sample dataset covering real world data problems (duplicates, nulls, PHI
masking, edge case names). The curriculum in `docs/lab-school/` maps every tool to its Microsoft
Fabric and Azure equivalent and covers the full stack from here to orchestration, distributed
processing, and a healthcare data lakehouse.

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
