---
title: "Advanced Sorting & Efficiency Trade-offs"
day: 6
date: "2024-02-05"
module: "Data Structures II"
pdfUrl: "/notes/dsa2-day6.pdf"
material: "https://github.com/ai-ml-iit-mandi/dsa2-sorting"
topics: ['Merge Sort', 'Quicksort', 'Algorithm Efficiency', 'Trade-offs']
---

# Advanced Sorting & Efficiency Trade-offs

To handle massive datasets, we must transcend elementary sorting. We introduce $O(N \log N)$ recursive sorting algorithms.

## Merge Sort vs Quicksort
- **Merge Sort:** A stable, divide-and-conquer algorithm. It consistently takes $O(N \log N)$ time but requires $O(N)$ extra space to merge sub-arrays.
- **Quicksort:** An in-place, unstable sort that partitions arrays around a pivot. It has an average time complexity of $O(N \log N)$ and space complexity of $O(\log N)$ (call stack), though worst-case is $O(N^2)$.

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

> [!NOTE]
> **Space-Time Trade-offs:** Selecting an algorithm is not just about time. In memory-constrained systems (embedded AI), Quicksort is preferred over Merge Sort due to its in-place sorting nature.
