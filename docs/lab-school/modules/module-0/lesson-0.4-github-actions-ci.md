# Lesson 0.4: Continuous integration with GitHub Actions

Module 0: Project setup and CI skeleton

## Concept
A GitHub Actions workflow is a YAML file in `.github/workflows/` that runs automatically on an
event. This one triggers on every push and pull request. It spins up a clean `ubuntu-latest` runner
(a fresh machine every time, which is what makes the result trustworthy), checks out the code, sets
up Python 3.12 to match local, installs the pinned `requirements.txt`, and runs `pytest`. A green
check means the tests ran and passed on a clean machine; a red mark flags the commit. The pinned
requirements file is what makes the run reproducible: CI installs the exact versions that passed
locally. Branch protection can require this check before a merge, so broken code cannot land.

## Why it matters
"My repo has CI gating from the first commit: every push runs the test suite on a clean runner, and
a failing check blocks the change."
