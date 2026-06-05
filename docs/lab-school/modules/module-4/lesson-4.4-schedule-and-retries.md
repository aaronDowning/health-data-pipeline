# Lesson 4.4: Schedule and retries

Module 4: Workflow orchestration with Airflow

## Concept
A DAG has a schedule that says when it runs, and its tasks can specify retries, how many times to
reattempt on failure, and backfill, running for past intervals that were missed. Retries are only
safe when a task is idempotent, the property from Module 1, because a retry reruns the task and it
must not duplicate or corrupt data on the second pass. This is where idempotency stops being theory
and becomes the reason orchestration can recover from failures automatically.

## Why it matters
"I schedule a DAG with retries and backfill, and I know retries are only safe because the tasks are
idempotent."
