# Lesson 7.3: Key checks

Module 7: Data quality and testing

## Concept
The checks that catch the most damage: no unexpected nulls in required fields, values within valid
ranges (an age is never negative), PHI is masked so no raw SSNs slip through, and referential
integrity so every encounter points to a real patient. Each check guards against a specific failure
mode, and choosing the right set is where a QA background pays off directly: you already think in
terms of what could go wrong and how to catch it.

## Why it matters
"I know which checks catch which failures: nulls, ranges, PHI masking, and referential integrity,
each guarding a specific corruption."
