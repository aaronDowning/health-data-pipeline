# Lesson 3.5.1: Why NoSQL

Module 3.5: NoSQL document store (MongoDB)

## Concept
A relational database requires a schema defined up front, which is schema on write: you declare the
tables and columns before any data lands. A document database stores flexible JSON documents and
interprets their structure when you read them, which is schema on read. FHIR bundles are JSON
documents of varying shape, so a document store is their natural landing place. The tradeoff:
documents are flexible and fast for ingesting raw data, while relational tables enforce structure and
are stronger for joins and analytics. Real pipelines use both, each for what it does best.

## Why it matters
"I can explain document versus relational and why raw FHIR fits a document store: schema on read for
flexible ingest, schema on write for structured analytics."
