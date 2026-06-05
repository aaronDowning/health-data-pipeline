# Lesson 3.2: Run Synthea

Module 3: Synthetic healthcare data (Synthea, FHIR, HL7)

## Concept
Synthea is an open source generator that produces realistic but entirely synthetic patient records
as FHIR bundles, with no real PHI. A bundle is a container that holds many resources for one patient:
the Patient resource itself plus their Encounters, Observations, and Conditions. This provides a
safe, realistic dataset shaped exactly like an Epic FHIR export, so the pipeline can practice on data
that looks real while carrying zero privacy risk.

## Why it matters
"I generate synthetic FHIR with Synthea, which gives realistic, HIPAA safe data shaped like a real
Epic export."
