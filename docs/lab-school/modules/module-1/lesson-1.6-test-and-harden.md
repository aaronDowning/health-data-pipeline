# Lesson 1.6: Test and harden

Module 1: Python ETL fundamentals

## Concept
Hardening makes a pipeline production worthy. Two parts. Edge case tests cover the inputs that break
pipelines silently: an empty input list, a record missing its name fields, a record with no PHI.
Data bugs rarely crash; they quietly corrupt, so tests are how you catch a transform that mishandles
a null. Logging adds observability: `pipeline.run` now logs the record count at each stage
(extracted, cleaned, de identified, loaded) so an unattended run can be inspected. The full suite is
13 tests.

## Why it matters
"We should harden data logic with edge case tests, because data bugs are silent corruptions rather than crashes, and adding stage by stage logging so an unattended run is observable."
