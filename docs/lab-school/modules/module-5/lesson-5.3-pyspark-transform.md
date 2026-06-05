# Lesson 5.3: PySpark transform

Module 5: Distributed processing with Spark and PySpark

## Concept
Rewrite the Module 1 transform in PySpark. The logic is the same (clean and de identify) but
expressed as DataFrame operations that run distributed across the cluster instead of looping row by
row in Python. Seeing the identical transform in both forms makes the pandas to PySpark differences
concrete: column operations over a whole DataFrame rather than per record Python, and execution
deferred until an action.

## Why it matters
"I have written the same transform in PySpark, so I can speak to the differences between single node
pandas and distributed DataFrame operations."
