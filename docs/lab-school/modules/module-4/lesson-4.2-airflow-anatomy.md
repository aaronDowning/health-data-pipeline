# Lesson 4.2: Airflow anatomy

Module 4: Workflow orchestration with Airflow

## Concept
Airflow has four parts that work together. The scheduler decides what should run and when. The
webserver serves the UI where you watch DAGs, runs, and logs. The executor actually runs the tasks.
The metadata database tracks the state of every run. Running it in Docker stands the whole thing up
locally. Understanding the parts is how you reason about why a task is queued, running, retrying, or
stuck, instead of treating the orchestrator as a black box.

## Why it matters
"I know Airflow's parts, the scheduler, webserver, executor, and metadata database, so I can reason
about why a task is queued or stuck."
