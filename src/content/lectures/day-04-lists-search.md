---
title: "Linked Lists & Binary Search"
day: 4
date: "2024-01-25"
module: "Data Structures I"
pdfUrl: "/notes/dsa1-day4.pdf"
material: "https://github.com/ai-ml-iit-mandi/dsa1-lists"
topics: ['Singly Linked Lists', 'Doubly Linked Lists', 'Binary Search', 'Divide & Conquer']
---

# Linked Lists & Binary Search

In this day's lecture, we contrast arrays with non-contiguous structures (Linked Lists) and look at the highly optimized Binary Search algorithm.

## Linked Lists
Unlike arrays, linked lists link nodes dynamically using pointers, bypassing the need for contiguous allocation.

```mermaid
graph LR
    Head[Head] --> A[Data: 10 | Next]
    A --> B[Data: 20 | Next]
    B --> C[Data: 30 | Next]
    C --> Null[NULL]
```

## Binary Search & Divide and Conquer
Binary Search reduces lookup from $O(N)$ to $O(\log N)$ by continuously cutting the search space in half. The array **MUST** be sorted.

```python
def binary_search(sorted_arr, target):
    low, high = 0, len(sorted_arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

> [!IMPORTANT]
> **Binary Search Invariant:** Each step eliminates half of the remaining search space. This logarithmic reduction is the base for more advanced tree searches in AI.
