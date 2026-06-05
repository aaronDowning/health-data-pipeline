# Lesson 2.1: Postgres in Docker

Module 2: PostgreSQL warehouse and SQL depth

## Concept
PostgreSQL runs as a container with a persistent volume. The volume maps the database's data
directory to storage on the host, so the container stays disposable while the data survives a
restart or a full recreate. The container exposes a port, and any client (psql, a GUI, or Python)
connects over it. This Postgres instance is the warehouse: the real Load target the pipeline writes
into, replacing the JSON file from Module 1. It builds directly on a homelab Docker background, where
containers, ports, and volumes are already second nature.

## Why it matters
"I run Postgres as a container with a persistent volume, so the database is reproducible and
disposable while the data itself survives restarts."

## Learn more
* Docker and PostgreSQL in 10 Minutes (Amigoscode): https://www.youtube.com/watch?v=aHbE3pTyG-Q
