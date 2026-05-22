---
title: "Python Basics & Core Syntax"
day: 1
date: "2024-01-15"
module: "Python Foundations"
pdfUrl: "/notes/python-day1.pdf"
material: "https://github.com/ai-ml-iit-mandi/python-foundations-day1"
topics: ['Variables & Data Types', 'Operators', 'Strings & Text Manipulation', 'Conditionals']
---

# Python Basics & Core Syntax

Welcome to the start of your journey in AI and Software Engineering! We begin with Python foundations, the absolute standard programming language for data science and AI.

## Variables & Data Types
In Python, variables are dynamically typed. This means you do not need to explicitly declare their type.

```python
# Core Data Types
age = 21                  # Integer
learning_rate = 0.001     # Float
course_title = "AI-ML"    # String
is_active = True          # Boolean
```

## Operators & Conditionals
We use standard arithmetic and logical operators to guide execution flow.

```python
# Check condition
if learning_rate < 0.01:
    print("Conservative optimization step size.")
elif learning_rate == 0.01:
    print("Standard step size.")
else:
    print("High risk of gradient explosion!")
```

> [!TIP]
> **Best Practice:** Keep variable names descriptive and follow standard PEP 8 naming conventions (snake_case for variables and functions).
