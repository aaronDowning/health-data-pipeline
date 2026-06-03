# Backlog and Known Limitations

Findings captured as we go, so nothing is silently ignored. Each gets fixed in a later module.

## clean_name corrupts names with non-letters (found in Lesson 0.3)
`src/transforms.py:clean_name` uses Python's `str.title()`, which capitalizes the letter after
any non-letter character. So "Aar0n" becomes "Aar0N", and "d'angelo" becomes "D'Angelo". Naive for
real names. Fix with a robust normalization approach in Module 1 (Python ETL transforms) and cover
it with automated data-quality checks in Module 7.
