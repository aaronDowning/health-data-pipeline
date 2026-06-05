# Lesson 8.1: CI vs CD

Module 8: CI/CD for the whole pipeline

## Concept
CI, continuous integration, runs the tests on every change to catch problems early. CD, continuous
delivery or deployment, takes a build that passed and ships it to the target automatically. The line
between them is where testing ends and deploying begins. For data infrastructure, CI validates the
pipeline code and its tests, and CD deploys the updated pipeline and services so the running system
reflects the latest passing commit.

## Why it matters
"I can draw the line between CI and CD: integration tests every change, delivery ships a passing
build to the target."
