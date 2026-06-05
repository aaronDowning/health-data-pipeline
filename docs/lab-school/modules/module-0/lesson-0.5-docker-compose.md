# Lesson 0.5: docker-compose skeleton

Module 0: Project setup and CI skeleton

## Concept
docker-compose describes a multi service stack as a single YAML file, so one command brings up the
whole environment instead of starting containers by hand. Three pieces matter: a service is a
container (a database, a web app, a worker), a volume persists data beyond the container lifecycle
so a restart does not wipe the database, and a network lets services find each other by name rather
than by IP. `docker compose up` starts everything, `docker compose down` stops it. This is the
backbone the later data services plug into: Postgres, MongoDB, Airflow, and MinIO all become
services in this one file. It builds directly on a homelab Docker background, where containers and
volumes are already familiar.

## Why it matters
"docker-compose defines a multi service stack as code: one file brings up the whole data platform,
with named services, persistent volumes, and a shared network."
