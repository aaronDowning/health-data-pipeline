# Lesson 2.6: EXPLAIN and indexes

Module 2: PostgreSQL warehouse and SQL depth

## Concept
EXPLAIN shows the query plan: how the database intends to fetch the data before it runs. A
sequential scan reads every row in a table, which is slow on large tables; an index scan jumps
straight to the matching rows. An index is a sorted lookup structure on a column that speeds reads,
at the cost of slower writes and extra storage, because the index has to be kept up to date. Reading
a plan tells you whether a query is doing expensive full scans and whether adding an index would
change the plan and the cost.

## Why it matters
"I read an EXPLAIN plan to spot expensive scans, and I know an index trades slower writes and more
storage for faster reads."

## Learn more
* SQL Execution Plans Visually Explained, SQL Course 40 (Data With Baraa): https://www.youtube.com/watch?v=O7AzUDogXsw
