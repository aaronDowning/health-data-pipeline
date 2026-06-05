# Lesson 7.4: Quality gate in the DAG

Module 7: Data quality and testing

## Concept
Wire the data quality checks into the Airflow DAG as a gate: if a record fails validation, the run
fails loudly instead of quietly loading corrupt data. This is the data equivalent of failing a build
on a red test. Failing loud beats silent corruption, because data that loads quietly but wrong is far
more expensive to discover and unwind later than a run that stops the moment something is off.

## Why it matters
"I gate the pipeline on data quality, so a bad record fails the run loudly rather than silently
corrupting the warehouse."
