# Lesson 8.4: Smoke test and protection

Module 8: CI/CD for the whole pipeline

## Concept
After a deploy, a smoke test triggers the DAG or a small pipeline run to confirm the new version
actually works, not merely that it deployed. Branch protection rules require the CI checks to pass
before code can merge, so broken code never reaches the main branch in the first place. Together they
make the whole path from commit to running pipeline safe: tested before merge, deployed on green, and
verified after deploy.

## Why it matters
"I smoke test after deploy and require passing checks before merge, so the path from commit to
running pipeline is verified, not assumed."
