# Lesson 1.3: Transform, clean

Module 1: Python ETL fundamentals

## Concept
Cleaning turns messy raw rows into consistent, trustworthy ones. `clean_name` trims and capitalizes
each word using `str.capitalize()` per word, which fixes the earlier `str.title()` bug that
corrupted names containing digits (so "Aar0n" stays "Aar0n"). It returns "" for missing or empty
names. `clean_record` returns a cleaned copy rather than mutating the original. `clean_records`
cleans every row and then drops duplicates by id, first occurrence wins. Order matters: clean before
dedupe so values like "  john " and "John" collapse to the same record, and handle nulls before any
step that assumes a value. Tests cover trimming and casing, the digit name fix, null handling, and
dedupe.

## Why it matters
"Transform is where data is reshaped, so it carries the most risk. I clean on a copy, fix casing
without corrupting digit or edge case names, handle nulls, and dedupe, with tests proving each rule."
