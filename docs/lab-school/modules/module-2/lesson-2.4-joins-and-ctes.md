# Lesson 2.4: JOINs and CTEs

Module 2: PostgreSQL warehouse and SQL depth

## Concept
A JOIN combines rows from two tables on a shared key. An inner join keeps only rows that match in
both tables; a left join keeps every row from the first table and fills nulls where the second has
no match. Picking the right join type is how you avoid silently dropping or duplicating records. A
CTE, the WITH clause, names a subquery so a complex query reads top to bottom as a sequence of named
steps instead of deeply nested parentheses, and it lets you reference the same intermediate result
more than once.

## Why it matters
"I query across tables with the right join type, and I use CTEs to make multi step queries readable
instead of deeply nested."

## Learn more
* SQL CTE Full Guide, the WITH Clause, SQL Course 28 (Data With Baraa): https://www.youtube.com/watch?v=5x1uodxEIaM
