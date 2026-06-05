# Lesson 4.1: Why orchestrate

Module 4: Workflow orchestration with Airflow

## Concept
A pipeline is a set of steps with dependencies: extract must finish before transform, transform
before load. Cron just fires a command on a clock with no awareness of order, success, or failure.
A DAG, a directed acyclic graph, models the steps as nodes and the dependencies as edges, so an
orchestrator runs them in the right order, waits for upstream success, and stops or retries on
failure. It is the same mental model as a CI pipeline's job graph, applied to data instead of builds.

## Why it matters
"I can explain why a DAG beats cron: it models dependencies and reacts to success and failure,
instead of just firing on a clock."
