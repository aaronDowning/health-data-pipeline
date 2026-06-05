# Lesson 8.2: Build and push images

Module 8: CI/CD for the whole pipeline

## Concept
GitHub Actions builds the pipeline's Docker images and pushes them to a registry, so the exact same
image that passed CI is the one that gets deployed. Containerizing the deploy means the running
environment matches the tested one, which eliminates works on my machine at the infrastructure level,
not just the dependency level. It is the same reproducibility instinct as pinning requirements, one
layer up: pin the whole environment, not just the packages.

## Why it matters
"I build and push Docker images in CI, so the exact tested image is what deploys, not a rebuilt
approximation."
