# Lesson 3.5.3: Land raw FHIR

Module 3.5: NoSQL document store (MongoDB)

## Concept
Store the Synthea FHIR bundles in MongoDB exactly as they arrive, as the raw bronze layer. Keeping
the raw data untouched means you can always reprocess it if a transform changes later, and it
preserves the original for audit. This is the bronze tier of the medallion pattern: raw, faithful,
and never edited in place. Downstream stages read from bronze and refine into the relational
warehouse rather than mutating the source.

## Why it matters
"I land raw FHIR in MongoDB as the bronze layer, keeping an untouched copy so the data can always be
reprocessed or audited."
