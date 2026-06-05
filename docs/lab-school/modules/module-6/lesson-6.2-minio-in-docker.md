# Lesson 6.2: MinIO in Docker

Module 6: Data lake and lakehouse (MinIO)

## Concept
MinIO is S3 compatible object storage that runs locally in Docker. Object storage holds files, the
objects, inside buckets and addresses each by a key, rather than storing rows in tables. It is cheap,
scalable, and the substrate most data lakes are built on. The raw FHIR bundles land here as the
bronze layer. MinIO maps to Azure Data Lake Storage and Fabric OneLake in the cloud, so the homelab
lake mirrors the managed one.

## Why it matters
"I run MinIO as S3 compatible object storage and use it as the lake's bronze layer, mapping to Azure
Data Lake Storage and OneLake."
