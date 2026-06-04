# Lesson 1.5: Load (and the end to end pipeline)

Module 1: Python ETL fundamentals

## Concept
Load writes the finished data to its destination; here the target is a JSON file (a database follows
in Module 2). `write_json` replaces the file rather than appending, which makes the load idempotent:
running the pipeline twice yields the same output, never duplicated rows. It also creates the target
directory if needed. `pipeline.run` wires the whole flow: extract (read_json), transform
(clean_records, then de_identify per row), load (write_json). Running it on the messy sample produced
clean, de identified records, including the "Aar0n" digit name preserved by the 1.3 fix. Tests cover
the end to end result, that output lands in the target, and idempotency.

## Why it matters
"Load writes the result with a replace, so the pipeline is idempotent. The run() function chains
extract, transform, and load into one reproducible flow, and tests prove running it twice never
duplicates data."
