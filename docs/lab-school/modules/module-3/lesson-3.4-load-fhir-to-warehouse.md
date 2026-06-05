# Lesson 3.4: Load FHIR to warehouse

Module 3: Synthetic healthcare data (Synthea, FHIR, HL7)

## Concept
This connects the flattened FHIR rows to the Postgres load from Module 2, completing an end to end
ingest: read FHIR bundles, flatten them to rows, clean and de identify, then load into the warehouse
tables. It mirrors how a real Epic FHIR export would land in a reporting warehouse. After this, the
pipeline runs on genuinely healthcare shaped data rather than the toy sample, and every earlier stage
(clean, de identify, idempotent load) now operates on real resource types.

## Why it matters
"I ingest synthetic FHIR end to end into a warehouse, the same shape an Epic FHIR export would take."
