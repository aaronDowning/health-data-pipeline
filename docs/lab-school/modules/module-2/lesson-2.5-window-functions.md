# Lesson 2.5: Window functions

Module 2: PostgreSQL warehouse and SQL depth

## Concept
A window function computes across a set of rows related to the current row without collapsing them,
which is the key difference from GROUP BY. GROUP BY reduces many rows to one per group; a window
function keeps every row and adds a computed column alongside it. The OVER clause defines the
window, with PARTITION BY to group and ORDER BY to sequence. Common uses are a running total, a rank
within a group, or comparing a row to the previous one. It is how you produce per patient running
counts or rankings while keeping each individual row visible.

## Why it matters
"I use window functions for running totals and rankings, which compute across rows without
collapsing them the way GROUP BY does."

## Learn more
* SQL Window Functions Basics, SQL Course 22 (Data With Baraa): https://www.youtube.com/watch?v=o666k19mZwE
