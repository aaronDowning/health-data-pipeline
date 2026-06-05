# Modules

Concept notes for each lab lesson, organized by module. Each lesson file holds the plain English
explanation and a key takeaway, captured for review.

Modules 0 and 1 were built hands on in lab sessions. Modules 2 through 9 are written ahead as
reference notes; hands on lab completion is tracked in PROGRESS.md.

Every lesson ends with a Learn more section that links videos for deeper study, with
[Data With Baraa](https://www.youtube.com/@DataWithBaraa) as the first source.

## Module 0: Project setup and CI skeleton
* Lesson 0.0: A real Python (not the system one)
* Lesson 0.1: Project structure
* Lesson 0.2: Virtual environments and dependencies
* Lesson 0.3: First pytest
* Lesson 0.4: Continuous integration with GitHub Actions
* Lesson 0.5: docker-compose skeleton

## Module 1: Python ETL fundamentals
* Lesson 1.1: The ETL model
* Lesson 1.2: Extract
* Lesson 1.3: Transform, clean
* Lesson 1.4: Transform, de identify
* Lesson 1.5: Load (end to end pipeline)
* Lesson 1.6: Test and harden

## Module 2: PostgreSQL warehouse and SQL depth
* Lesson 2.1: Postgres in Docker
* Lesson 2.2: Schema modeling
* Lesson 2.3: Load via SQLAlchemy
* Lesson 2.4: JOINs and CTEs
* Lesson 2.5: Window functions
* Lesson 2.6: EXPLAIN and indexes

## Module 3: Synthetic healthcare data (Synthea, FHIR, HL7)
* Lesson 3.1: EHR, FHIR, HL7, REDCap
* Lesson 3.2: Run Synthea
* Lesson 3.3: Parse and flatten FHIR
* Lesson 3.4: Load FHIR to warehouse

## Module 3.5: NoSQL document store (MongoDB)
* Lesson 3.5.1: Why NoSQL
* Lesson 3.5.2: MongoDB in Docker
* Lesson 3.5.3: Land raw FHIR
* Lesson 3.5.4: Query and index

## Module 4: Workflow orchestration with Airflow
* Lesson 4.1: Why orchestrate
* Lesson 4.2: Airflow anatomy
* Lesson 4.3: First DAG
* Lesson 4.4: Schedule and retries
* Lesson 4.5: Pipeline as DAG

## Module 5: Distributed processing with Spark and PySpark
* Lesson 5.1: Why Spark
* Lesson 5.2: Spark basics
* Lesson 5.3: PySpark transform
* Lesson 5.4: Optimization

## Module 6: Data lake and lakehouse (MinIO)
* Lesson 6.1: Lake vs warehouse vs lakehouse
* Lesson 6.2: MinIO in Docker
* Lesson 6.3: Medallion layers

## Module 7: Data quality and testing
* Lesson 7.1: Data contracts
* Lesson 7.2: Great Expectations
* Lesson 7.3: Key checks
* Lesson 7.4: Quality gate in the DAG

## Module 7.5: Analytics dashboard
* Lesson 7.5.1: Dashboard on gold
* Lesson 7.5.2: An outcome report

## Module 8: CI/CD for the whole pipeline
* Lesson 8.1: CI vs CD
* Lesson 8.2: Build and push images
* Lesson 8.3: Deploy to the homelab
* Lesson 8.4: Smoke test and protection

## Module 9: Capstone and demo
* Lesson 9.1: README and diagram
* Lesson 9.2: Technical demo
* Lesson 9.3: Stakeholder narration
* Lesson 9.4: Dry run
