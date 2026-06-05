# Lesson 4.5: Pipeline as DAG

Module 4: Workflow orchestration with Airflow

## Concept
This wires the whole pipeline (generate, extract, transform, load, validate) into one Airflow DAG,
each stage a task with the right dependencies. It turns the single script from Module 1 into an
orchestrated, scheduled, observable pipeline that recovers from failures and shows its run history in
the UI. This is the same shape that Azure Data Factory and Fabric Data Pipelines run in the cloud, so
the homelab DAG maps directly to the managed equivalent.

## Why it matters
"I orchestrate the full pipeline as a DAG, which maps directly to Azure Data Factory and Fabric Data
Pipelines."
