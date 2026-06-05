# Lesson 5.2: Spark basics

Module 5: Distributed processing with Spark and PySpark

## Concept
Spark works on DataFrames, similar to pandas but distributed across the cluster. The key idea is lazy
evaluation: transformations are recorded into a plan but not executed until an action, like writing
output or counting rows, triggers them. Laziness lets Spark see the whole chain of operations and
optimize it before running anything. Running Spark in Docker is enough to experiment with DataFrame
operations and watch when execution actually happens.

## Why it matters
"I work with Spark DataFrames and understand lazy evaluation: transformations build a plan that runs
only when an action triggers it."
