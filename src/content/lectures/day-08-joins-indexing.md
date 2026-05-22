---
title: "Joins, Indexing & Query Optimization"
day: 8
date: "2024-02-15"
module: "Database Engineering and Schema Design"
pdfUrl: "/notes/db-day8.pdf"
material: "https://github.com/ai-ml-iit-mandi/db-optimization"
topics: ['SQL Joins', 'B-Tree Indexing', 'Query Plans', 'Optimization']
---

# Joins, Indexing & Query Optimization

Retrieving data efficiently is as important as structuring it correctly. We explore the inner mechanics of Joins and Indexing structures.

## SQL Joins
We merge tables using common columns.

- **INNER JOIN:** Returns records with matching values in both tables.
- **LEFT (OUTER) JOIN:** Returns all records from the left table, and matched records from the right.
- **FULL JOIN:** Returns all records when there is a match in either table.

```sql
SELECT Students.name, Enrollment.course_name
FROM Students
INNER JOIN Enrollment ON Students.student_id = Enrollment.student_id;
```

## Database Indexing (B-Trees)
Without an index, a query requires a full table scan ($O(N)$ search). Creating an index creates a B-Tree structure, accelerating lookups to $O(\log N)$ search complexity.

> [!CAUTION]
> **Indexing Overhead:** Indexes make `SELECT` queries extremely fast, but slow down write operations (`INSERT`, `UPDATE`, `DELETE`) because the database must update the B-Tree for every change!
