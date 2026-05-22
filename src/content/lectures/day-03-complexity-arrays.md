---
title: "Algorithmic Complexity & Arrays"
day: 3
date: "2024-01-22"
module: "Data Structures I"
pdfUrl: "/notes/dsa1-day3.pdf"
material: "https://github.com/ai-ml-iit-mandi/dsa1-arrays"
topics: ['Big-O Notation', 'Time Complexity', 'Space Complexity', 'Arrays & Vectors']
---

# Algorithmic Complexity & Arrays

Before writing code for massive scale, we must learn to evaluate its efficiency. This session introduces asymptotic analysis and contiguous memory arrays.

## Big-O Notation
Big-O notation describes the upper bound of execution time or space usage in terms of input size $N$.

| Complexity | Name | Example Operation |
|------------|------|-------------------|
| $O(1)$ | Constant | Accessing array element by index |
| $O(\log N)$| Logarithmic | Binary search |
| $O(N)$ | Linear | Iterating through an array once |
| $O(N \log N)$| Linearithmic | Merge sort, Quicksort |
| $O(N^2)$ | Quadratic | Nested loops (Bubble Sort) |

## Contiguous Memory & Arrays
Arrays store elements in consecutive memory addresses, making index-based lookup incredibly fast ($O(1)$) but insertions/deletions expensive ($O(N)$).

```python
# Array insertion example
arr = [10, 20, 30, 40]
arr.insert(1, 15)  # Shifts 20, 30, 40 -> O(N) complexity
```

> [!WARNING]
> **Dynamic Arrays:** Python lists are dynamic arrays under the hood. They allocate excess memory capacity upfront to guarantee amortized $O(1)$ insertions at the end.
