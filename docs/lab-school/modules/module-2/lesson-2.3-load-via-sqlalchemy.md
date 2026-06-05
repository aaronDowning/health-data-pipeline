# Lesson 2.3: Load via SQLAlchemy

Module 2: PostgreSQL warehouse and SQL depth

## Concept
SQLAlchemy connects Python to Postgres through an engine, which manages a pool of connections, and
executes inserts with parameterized statements. Parameterized means the values are passed
separately from the SQL text, so the database never confuses data for code; this is what prevents
SQL injection, the same input trust instinct from QA. This replaces the file based `write_json` from
Module 1 with a real database Load, and it keeps the idempotent intent: upsert or replace on a key
rather than blindly append, so a rerun does not duplicate rows.

## Why it matters
"I load into Postgres through SQLAlchemy with parameterized inserts, keeping the load idempotent and
safe from SQL injection."

## Learn more
* SQLAlchemy Crash Course, Master Databases in Python: https://www.youtube.com/watch?v=529LYDgRTgQ
