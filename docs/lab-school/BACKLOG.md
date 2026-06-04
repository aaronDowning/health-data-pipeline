# Backlog and Known Limitations

Findings captured as we go, so nothing is silently ignored. Each gets fixed in a later module.

## clean_name corrupts names with non-letters (found 0.3, RESOLVED 1.3)
The original `src/transforms.py:clean_name` used Python's `str.title()`, which capitalizes the
letter after any non-letter character. So "Aar0n" became "Aar0N". Naive for real names.

Resolved in Lesson 1.3: `src/transform.py:clean_name` now capitalizes per word with
`str.capitalize()`, which does not treat digits as word boundaries, so "Aar0n" stays "Aar0n". A
test covers it, and the old throwaway `transforms.py` was removed. Apostrophe and hyphen names
(O'Brien, Mary-Jane) remain a lighter known limitation for a future locale aware pass.
