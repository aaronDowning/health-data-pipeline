# Lesson 0.3: First pytest

Module 0: Project setup and CI skeleton

## Concept
pytest is Python's test runner, and it is lighter than the JS runners. Three differences from
Playwright or Jest: you use a plain `assert` statement instead of an `expect().toBe()` matcher
library (pytest rewrites the assert so a failure still prints a rich diff), tests are discovered by
naming convention (files `test_*.py`, functions `test_*`) with no spec config, and a test is just a
plain function with no describe or it wrapper. A `pytest.ini` with `pythonpath = src` lets the tests
import the code under test cleanly. Run `pytest` from the repo root and it collects and runs
everything it discovers.

## Real find this lesson
Probing an edge case (a name with a digit) showed that `str.title()` capitalizes the letter after
any non-letter, so "Aar0n" becomes "Aar0N". The same issue hits apostrophes. Naive name cleaning
corrupts real data. Logged to BACKLOG for a robust transform in Module 1.

## Talking point
"I write pytest with plain asserts and convention based discovery, and my QA instinct catches
data-corrupting edge cases early, like title-casing breaking names that contain digits or apostrophes."
