# Lesson 3.3: Parse and flatten FHIR

Module 3: Synthetic healthcare data (Synthea, FHIR, HL7)

## Concept
FHIR resources are deeply nested JSON. Flattening means walking that nested structure and pulling
the fields that matter into flat relational rows, mapping each resource type to a table: Patient to a
patients table, Encounter to an encounters table. The real work is navigating the nesting and
handling optional or missing fields, which is exactly the transform risk from Module 1, where
mishandling a missing value silently corrupts a row. The output is tabular rows ready for the
warehouse.

## Why it matters
"I parse nested FHIR JSON and flatten each resource type into relational rows, handling the optional
fields that nested health data is full of."
