# Lesson 8.3: Deploy to the homelab

Module 8: CI/CD for the whole pipeline

## Concept
Deploy the updated stack to the homelab host, either with a self hosted GitHub Actions runner or an
SSH deploy step that pulls the new images and restarts the compose stack. Secrets such as keys and
connection strings are injected securely from the CI environment and never committed to the repo.
This is the CD half in practice: a push results in the homelab running the new version, with the
secret handling kept outside source control.

## Why it matters
"I deploy the stack to the homelab from CI with secure secret handling, so a push refreshes the
running pipeline."
