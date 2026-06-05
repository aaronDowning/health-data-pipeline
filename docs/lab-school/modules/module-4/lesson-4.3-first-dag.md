# Lesson 4.3: First DAG

Module 4: Workflow orchestration with Airflow

## Concept
A DAG is defined in Python: tasks plus the dependencies between them. Each task is an operator, for
example one that runs a Python function or a shell command. Dependencies are declared explicitly (a
task runs after another), and the scheduler executes them in that order. This is the same job graph
model as a CI pipeline, just expressed in Python and aimed at data work rather than builds and tests.

## Why it matters
"I define a DAG as tasks and dependencies in Python, the same job graph model as CI, applied to
data."
