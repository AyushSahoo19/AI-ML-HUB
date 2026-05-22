---
title: "Loops, Functions & Core Data Structures"
day: 2
date: "2024-01-18"
module: "Python Foundations"
pdfUrl: "/notes/python-day2.pdf"
material: "https://github.com/ai-ml-iit-mandi/python-foundations-day2"
topics: ['Loops & Conditionals', 'Defining Functions', 'Core Data Structures', 'File Handling']
---

# Loops, Functions & Core Data Structures

Building on syntax, we now look at handling repetitions, organizing code into reusable blocks, and utilizing Python's extremely powerful built-in data structures.

## Iteration & Loops
Python offers `for` and `while` loops to traverse datasets.

```python
# Looping through a list of hyper-parameters
epochs = [10, 50, 100, 200]
for num_epochs in epochs:
    print(f"Training model for {num_epochs} epochs...")
```

## Functions & Data Structures
Functions help us abstract logic. Python's core data structures (Lists, Tuples, Dictionaries, Sets) are the building blocks of data manipulation.

```python
# Dynamic helper function
def calculate_accuracy(y_true, y_pred):
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true)

# Dictionary representing student profile
student = {
    "name": "Arjun",
    "completed_days": 2,
    "scores": [95, 88]
}
```

> [!NOTE]
> **File Handling:** Python makes file manipulation trivial using context managers (`with` statement) which guarantee files are closed properly after execution.
