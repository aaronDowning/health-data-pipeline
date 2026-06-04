# Lesson 1.2: Extract

Module 1: Python ETL fundamentals

## Concept
Extract has one job: get the raw data into memory reliably, as is, with no cleaning or reshaping.
`read_json` opens a JSON file and parses it with Python's `json` module; a JSON array becomes a list
and each JSON object becomes a dict, so the result is a list of dicts. The key design rule is to
isolate extraction from the rest of the pipeline, so that when the source changes (a different file
format, an API, a new vendor) only the extract step changes and Transform and Load never notice.
This is the same instinct as a page object or API client layer in test automation: wall off how the
data is fetched.

## Why it matters
"Extraction is isolated on purpose: it just pulls raw data into memory, so a source change touches
only one step and never ripples into transform or load."
