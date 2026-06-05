# Lesson 7.2: Great Expectations

Module 7: Data quality and testing

## Concept
Great Expectations (or dbt tests) is a framework for declaring data expectations as suites and
running them against the data, producing a pass or fail report. An expectation is a single rule, such
as this column has no nulls or these values fall within a range. A suite groups many expectations
together. It turns data quality from scattered ad hoc checks into a repeatable, automated validation
step that runs as part of the pipeline.

## Why it matters
"I set up an expectation suite that validates data against declared rules, turning quality checks
into repeatable automation."
