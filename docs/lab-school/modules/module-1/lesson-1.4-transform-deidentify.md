# Lesson 1.4: Transform, de identify

Module 1: Python ETL fundamentals

## Concept
De identification removes or obscures PHI so a record cannot be traced to a real person, and it runs
inside Transform, before Load, so raw identifiers never reach the destination. Two HIPAA Safe Harbor
techniques: masking (`mask_ssn` hides all but the last 4 digits of an SSN) and generalization
(`to_birth_year` coarsens a full birth date to just the year). `de_identify` works on a copy, so the
raw record is never mutated; it masks the SSN and replaces the precise birth date with a birth year.
Tests confirm the masking, the generalization, the removed field, and that the original is untouched.

## Why it matters
"De identification happens in transform, before load, so PHI never lands downstream. I mask direct
identifiers like SSNs and generalize dates, on a copy, with tests proving the raw data is never
mutated."
