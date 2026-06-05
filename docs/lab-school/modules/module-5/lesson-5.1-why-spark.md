# Lesson 5.1: Why Spark

Module 5: Distributed processing with Spark and PySpark

## Concept
pandas processes data on a single machine, in memory. When the data is bigger than one machine's
memory, you need distributed processing. Spark splits the work across a cluster, where each machine
handles a partition of the data, like a kitchen of chefs splitting the prep instead of one chef
doing all of it. It is the same instinct as parallel test execution, spreading work across workers.
Spark wins specifically when the data exceeds a single node; for small data, pandas is simpler and
faster.

## Why it matters
"I can explain when Spark beats pandas: data larger than one machine's memory, split across a cluster
like parallel test execution."
