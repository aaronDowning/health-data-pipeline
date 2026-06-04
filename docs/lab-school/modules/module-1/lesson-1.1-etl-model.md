# Lesson 1.1: The ETL model

Module 1: Python ETL fundamentals

## Concept
ETL has three stages. Extract pulls data out of a source (a file, an API, a database). Transform
reshapes the raw data into something clean and usable: dedupe, fix types, handle nulls, validate,
and de identify. Load writes the finished data to its destination, such as a warehouse table. The
logic concentrates in Transform; Extract and Load are mostly plumbing, while Transform is where most
of the code and most of the risk live, because changing data is exactly where it can be mutated
incorrectly. Modern systems sometimes flip the order to ELT, loading raw data first and transforming
it inside the warehouse, which shows up later as the bronze, silver, and gold layers.

## Why it matters
"ETL is extract, transform, load, and the transform stage carries the most code and the most risk.
A quality mindset there, validating that data was not silently corrupted, is what keeps a pipeline
trustworthy."
