# Lesson 3.5.2: MongoDB in Docker

Module 3.5: NoSQL document store (MongoDB)

## Concept
MongoDB runs as a container with a persistent volume, the same pattern as Postgres. Its data model
differs: a database holds collections, and a collection holds documents, where Postgres has schemas,
tables, and rows. A document is just JSON (stored as BSON internally), so a FHIR bundle drops in with
no table definition required first. Mapping the two models against each other (collection equals
table, document equals row, with no fixed columns) is the fastest way to get oriented coming from a
relational background.

## Why it matters
"I run MongoDB in Docker and can map its model to the relational one: collections and documents
instead of tables and rows."
