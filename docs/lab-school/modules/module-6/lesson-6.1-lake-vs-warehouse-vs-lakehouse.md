# Lesson 6.1: Lake vs warehouse vs lakehouse

Module 6: Data lake and lakehouse (MinIO)

## Concept
A data warehouse stores structured, modeled data for fast SQL analytics, defined schema on write. A
data lake stores raw files of any shape, structured or not, cheaply, with structure interpreted
schema on read. A lakehouse combines the two: lake storage with warehouse style structure and
querying layered on top, as in Delta or Fabric OneLake. Each fits a different need: the lake for raw
and flexible, the warehouse for clean and queryable, the lakehouse for both at once.

## Why it matters
"I can distinguish lake, warehouse, and lakehouse: raw flexible storage, structured analytics, and
the hybrid that does both."
