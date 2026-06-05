# Lesson 2.2: Schema modeling

Module 2: PostgreSQL warehouse and SQL depth

## Concept
Modeling means deciding the tables and how they relate: patients, encounters, and observations,
each with a primary key and foreign keys that link a row back to its patient. Two common shapes. A
normalized model stores each fact once and joins on keys, which protects integrity and suits writes.
A star schema puts a central fact table around dimension tables, which suits analytics and fast
reads. Keys are what enforce the relationships and prevent orphaned rows. Choosing a shape is a
tradeoff between write integrity and read simplicity.

## Why it matters
"We model the warehouse with primary and foreign keys"

## Learn more
* BI Data Modeling: Star Schema, Snowflake and Galaxy (Data With Baraa): https://www.youtube.com/watch?v=TtxfKIe0HuQ
