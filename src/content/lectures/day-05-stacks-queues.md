---
title: "Stacks, Queues & Elementary Sorting"
day: 5
date: "2024-02-01"
module: "Data Structures II"
pdfUrl: "/notes/dsa2-day5.pdf"
material: "https://github.com/ai-ml-iit-mandi/dsa2-stacks"
topics: ['Stacks (LIFO)', 'Queues (FIFO)', 'Bubble Sort', 'Insertion Sort']
---

# Stacks, Queues & Elementary Sorting

We now explore restricted linear structures and elementary sorting mechanisms, highlighting the physical and computational trade-offs.

## Stacks & Queues
- **Stack (Last-In-First-Out / LIFO):** Operations include `push` and `pop`. Excellent for recursion management and undo operations.
- **Queue (First-In-First-Out / FIFO):** Operations include `enqueue` and `dequeue`. Essential for breadth-first search and task schedulers.

```python
# Stack Implementation using List
stack = []
stack.append("State A")  # Push
state = stack.pop()      # Pop -> "State A"

# Queue Implementation using deque
from collections import deque
queue = deque([])
queue.append("Task 1")   # Enqueue
task = queue.popleft()   # Dequeue -> "Task 1"
```

## Elementary Sorting
Bubble Sort and Insertion Sort are intuitive, $O(N^2)$ average-case sorting routines. While inefficient for large $N$, Insertion Sort is incredibly fast for nearly-sorted data.
