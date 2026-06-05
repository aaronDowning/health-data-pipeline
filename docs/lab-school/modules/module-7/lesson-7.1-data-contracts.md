# Lesson 7.1: Data contracts

Module 7: Data quality and testing

## Concept
A data contract is an agreed set of expectations about data: which fields exist, what types they
are, what ranges are valid, and that keys are unique. It is the data world's version of a test
assertion. Validating against a contract catches bad data at the boundary instead of letting it flow
downstream and corrupt everything it touches. This is the QA mindset applied to data: define what
good looks like, then enforce it automatically.

## Why it matters
"A data contract is an assertion about data shape and validity, the QA instinct applied to pipelines:
define good, then enforce it."
