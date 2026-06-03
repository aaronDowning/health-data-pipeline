# Lesson 0.1: Project structure

Module 0: Project setup and CI skeleton

## Concept
A clean repo separates three things: the code that does the work (`src/`), the code that proves
it works (`tests/`), and the docs that orient a human (`README.md`). Same instinct as a Playwright
framework, where page objects, specs, and config live in predictable homes so automation and the
next person can find them. In a data project the pipeline is the product and the tests prove it,
so "the code" becomes `src/` plus `tests/`. A `.gitignore` keeps junk, secrets, and (critically in
healthcare) data out of git history. Ignoring `data/` is a HIPAA guardrail: never let patient data
into a repo.

## Why it matters
"I scaffolded the repo with clean structure and a HIPAA safe gitignore from commit one."
