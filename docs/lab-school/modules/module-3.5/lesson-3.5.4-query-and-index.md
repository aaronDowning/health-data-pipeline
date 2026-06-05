# Lesson 3.5.4: Query and index

Module 3.5: NoSQL document store (MongoDB)

## Concept
MongoDB finds documents with a JSON style filter, and an aggregation pipeline transforms and groups
them, which is the document world's version of SQL. An index on a field speeds those queries the
same way a Postgres index does, with the same write cost tradeoff. This is enough to pull specific
resources out of the raw bronze documents before flattening them downstream, so the document store
is not just a dumping ground but a queryable raw layer.

## Why it matters
"I query and aggregate Mongo documents and add indexes, the document store parallel to SQL queries
and Postgres indexes."
