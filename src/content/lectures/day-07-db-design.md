---
title: "Relational Databases & Schema Design"
day: 7
date: "2024-02-12"
module: "Database Engineering and Schema Design"
pdfUrl: "/notes/db-day7.pdf"
material: "https://github.com/ai-ml-iit-mandi/db-schema"
topics: ['Relational Model', 'SQL DDL', 'Entity-Relationship (ER)', 'Normalization (1NF-3NF)']
---

# Relational Databases & Schema Design

Relational databases serve as the structural backbone of enterprise data infrastructure. Here, we cover schema design, entities, and database normalization.

## Entity-Relationship Modeling
We map real-world objects into database tables with columns (attributes) and establish primary keys and foreign keys.

```sql
-- DDL Example
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE Enrollment (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_name VARCHAR(100),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);
```

## Normalization (1NF, 2NF, 3NF)
Normalization eliminates data redundancy and prevents insertion, update, and deletion anomalies by decomposing tables.
1. **First Normal Form (1NF):** Atomic values only, no repeating groups.
2. **Second Normal Form (2NF):** In 1NF and no partial dependencies (every non-key attribute depends on the *entire* primary key).
3. **Third Normal Form (3NF):** In 2NF and no transitive dependencies (non-key attributes cannot depend on other non-key attributes).
