# Lesson 6.3: Medallion layers

Module 6: Data lake and lakehouse (MinIO)

## Concept
The medallion architecture refines data in tiers. Bronze is raw, ingested exactly as it arrived.
Silver is cleaned, standardized, and de identified. Gold is business ready, modeled into a star
schema for reporting. Data flows bronze to silver to gold, each tier more refined and more
trustworthy than the last. This is the structure that ties the lake (raw bronze) to the warehouse
(gold), and it maps directly to how Fabric and Delta organize data.

## Why it matters
"I structure data as a medallion: raw bronze, cleaned silver, business ready gold, the standard
refinement pattern in Fabric and Delta."
