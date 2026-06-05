# Lesson 5.4: Optimization

Module 5: Distributed processing with Spark and PySpark

## Concept
Spark performance comes down to a few levers. Partitioning controls how the data is split across the
cluster, which sets how much parallelism you get. A shuffle moves data between machines, which a join
or a group by requires, and it is the expensive operation, so you design to minimize it. Caching
keeps a reused DataFrame in memory rather than recomputing it from the plan each time. Knowing these
three (partitioning, shuffles, caching) is enough to speak credibly to optimizing a Spark job.

## Why it matters
"I can name the main Spark optimization levers, partitioning, minimizing shuffles, and caching, and
explain why shuffles are costly."
