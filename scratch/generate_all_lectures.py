import os
import shutil

# Path to lectures directory
lectures_dir = r"c:\Users\ayush\OneDrive\Desktop\AI ML IIT Mandi\03_Website\src\content\lectures"

# Ensure directory exists, clean it up
if os.path.exists(lectures_dir):
    shutil.rmtree(lectures_dir)
os.makedirs(lectures_dir)

lectures_data = [
    {
        "filename": "day-01-python-foundations.md",
        "title": "Python Basics & Core Syntax",
        "day": 1,
        "date": "2024-01-15",
        "module": "Python Foundations",
        "pdfUrl": "/notes/python-day1.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/python-foundations-day1",
        "topics": ["Variables & Data Types", "Operators", "Strings & Text Manipulation", "Conditionals"],
        "content": """# Python Basics & Core Syntax

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
"""
    },
    {
        "filename": "day-02-loops-functions.md",
        "title": "Loops, Functions & Core Data Structures",
        "day": 2,
        "date": "2024-01-18",
        "module": "Python Foundations",
        "pdfUrl": "/notes/python-day2.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/python-foundations-day2",
        "topics": ["Loops & Conditionals", "Defining Functions", "Core Data Structures", "File Handling"],
        "content": """# Loops, Functions & Core Data Structures

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
"""
    },
    {
        "filename": "day-03-complexity-arrays.md",
        "title": "Algorithmic Complexity & Arrays",
        "day": 3,
        "date": "2024-01-22",
        "module": "Data Structures I",
        "pdfUrl": "/notes/dsa1-day3.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/dsa1-arrays",
        "topics": ["Big-O Notation", "Time Complexity", "Space Complexity", "Arrays & Vectors"],
        "content": """# Algorithmic Complexity & Arrays

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
"""
    },
    {
        "filename": "day-04-lists-search.md",
        "title": "Linked Lists & Binary Search",
        "day": 4,
        "date": "2024-01-25",
        "module": "Data Structures I",
        "pdfUrl": "/notes/dsa1-day4.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/dsa1-lists",
        "topics": ["Singly Linked Lists", "Doubly Linked Lists", "Binary Search", "Divide & Conquer"],
        "content": """# Linked Lists & Binary Search

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
"""
    },
    {
        "filename": "day-05-stacks-queues.md",
        "title": "Stacks, Queues & Elementary Sorting",
        "day": 5,
        "date": "2024-02-01",
        "module": "Data Structures II",
        "pdfUrl": "/notes/dsa2-day5.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/dsa2-stacks",
        "topics": ["Stacks (LIFO)", "Queues (FIFO)", "Bubble Sort", "Insertion Sort"],
        "content": """# Stacks, Queues & Elementary Sorting

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
"""
    },
    {
        "filename": "day-06-advanced-sorting.md",
        "title": "Advanced Sorting & Efficiency Trade-offs",
        "day": 6,
        "date": "2024-02-05",
        "module": "Data Structures II",
        "pdfUrl": "/notes/dsa2-day6.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/dsa2-sorting",
        "topics": ["Merge Sort", "Quicksort", "Algorithm Efficiency", "Trade-offs"],
        "content": """# Advanced Sorting & Efficiency Trade-offs

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
"""
    },
    {
        "filename": "day-07-db-design.md",
        "title": "Relational Databases & Schema Design",
        "day": 7,
        "date": "2024-02-12",
        "module": "Database Engineering and Schema Design",
        "pdfUrl": "/notes/db-day7.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/db-schema",
        "topics": ["Relational Model", "SQL DDL", "Entity-Relationship (ER)", "Normalization (1NF-3NF)"],
        "content": """# Relational Databases & Schema Design

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
"""
    },
    {
        "filename": "day-08-joins-indexing.md",
        "title": "Joins, Indexing & Query Optimization",
        "day": 8,
        "date": "2024-02-15",
        "module": "Database Engineering and Schema Design",
        "pdfUrl": "/notes/db-day8.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/db-optimization",
        "topics": ["SQL Joins", "B-Tree Indexing", "Query Plans", "Optimization"],
        "content": """# Joins, Indexing & Query Optimization

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
"""
    },
    {
        "filename": "day-09-supervised-regression.md",
        "title": "Supervised Learning & Regression Models",
        "day": 9,
        "date": "2024-02-22",
        "module": "Fundamentals of Classical Machine Learning",
        "pdfUrl": "/notes/ml-day9.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/ml-regression",
        "topics": ["Supervised Learning", "Linear Regression", "Gradient Descent", "Evaluation Metrics"],
        "content": """# Supervised Learning & Regression Models

We step into the realm of Machine Learning, transitioning from deterministic algorithms to statistical inference models.

## Linear Regression
Linear Regression assumes a linear relationship between input features $X$ and a continuous target $y$:
$$y = w X + b$$
Where $w$ represents weights, and $b$ is the bias.

## Gradient Descent
To train the model, we minimize a Loss Function (e.g., Mean Squared Error) using Gradient Descent, taking iterative steps in the opposite direction of the gradient.

```python
# Simple linear regression gradient descent step
w = w - learning_rate * gradient_w
b = b - learning_rate * gradient_b
```

## Evaluation Metrics
- **Mean Squared Error (MSE):** Emphasizes larger errors.
- **Root Mean Squared Error (RMSE):** In the same units as the target.
- **R-squared ($R^2$):** Measures the proportion of variance explained by the model.
"""
    },
    {
        "filename": "day-10-ensembles-pca.md",
        "title": "Ensemble Methods & Unsupervised Learning",
        "day": 10,
        "date": "2024-02-26",
        "module": "Fundamentals of Classical Machine Learning",
        "pdfUrl": "/notes/ml-day10.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/ml-advanced",
        "topics": ["Decision Trees", "Random Forests", "K-Means Clustering", "PCA Dimensionality"],
        "content": """# Ensemble Methods & Unsupervised Learning

In this lecture, we cover high-performance non-linear classifiers (Decision Trees, Random Forests) and dive into Unsupervised Learning.

## Ensemble Methods: Random Forest
A single Decision Tree is highly prone to overfitting. A **Random Forest** solves this by training hundreds of individual trees on random subsets of the data and features (Bagging), then voting or averaging their outputs.

## Unsupervised Learning & PCA
When we have no label $y$, we search for underlying structure.

- **K-Means Clustering:** Groups data points into $K$ spherical clusters based on spatial proximity.
- **Principal Component Analysis (PCA):** Projects high-dimensional datasets onto lower-dimensional subspaces while retaining maximum variance.

```python
from sklearn.decomposition import PCA
# Reduce 100 features to 2 principal components for visualization
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_high_dim)
```
"""
    },
    {
        "filename": "day-11-deep-learning-mlp.md",
        "title": "Neural Network Foundations & MLP",
        "day": 11,
        "date": "2024-03-05",
        "module": "Fundamentals of Deep Learning",
        "pdfUrl": "/notes/dl-day11.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/dl-mlp",
        "topics": ["Artificial Neurons", "Multi-Layer Perceptrons", "Activation Functions", "Backpropagation"],
        "content": """# Neural Network Foundations & MLP

Deep Learning models represent high-level representations through layered abstract connections, simulating biological cognitive pathways.

## Multi-Layer Perceptrons (MLPs)
An MLP is a forward-feeding neural structure consisting of an Input layer, one or more Hidden layers, and an Output layer.

```mermaid
graph LR
    I[Input X] --> H[Hidden Layer]
    H --> O[Output Y]
```

## Backpropagation & Optimization
The error is propagated backward through the network using the mathematical **Chain Rule** to compute gradients of the loss with respect to all weights and biases.

```python
# PyTorch simple implementation
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

> [!TIP]
> **Activation Functions:** Non-linear activation functions (ReLU, Sigmoid, Tanh) are crucial. Without them, a multi-layer neural network collapses into a single linear transformation!
"""
    },
    {
        "filename": "day-12-cnn-sequences.md",
        "title": "CNNs, LSTMs & Transformer Basics",
        "day": 12,
        "date": "2024-03-10",
        "module": "Fundamentals of Deep Learning",
        "pdfUrl": "/notes/dl-day12.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/dl-cnn",
        "topics": ["CNNs for Vision", "LSTMs & RNNs", "Self-Attention", "Deep Architectures"],
        "content": """# CNNs, LSTMs & Transformer Basics

Standard MLPs struggle with spatial images and sequential text. We study structural neural architectures.

## Convolutional Neural Networks (CNNs)
CNNs utilize overlapping kernel filters to capture local spatial details (edges, shapes) across input images, maintaining translation invariance.

## Recurrent Networks & Transformers
- **RNNs & LSTMs:** Maintain sequential memory cells to process sequences (time-series, texts), but suffer from vanishing gradients.
- **Transformers:** Resolve sequential bottlenecks by executing a **Self-Attention** matrix, computing relationships across all inputs simultaneously.
"""
    },
    {
        "filename": "day-13-llm-pretraining.md",
        "title": "Large Language Models & Pretraining",
        "day": 13,
        "date": "2024-03-18",
        "module": "Generative AI and Foundation Models",
        "pdfUrl": "/notes/genai-day13.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/genai-foundations",
        "topics": ["Transformers", "BERT vs GPT", "LLaMA & CLIP", "Multimodal Pretraining"],
        "content": """# Large Language Models & Pretraining

We enter the frontier of Generative AI, inspecting how modern massive foundation models are pretrained.

## BERT vs GPT
- **BERT (Encoder-only):** Uses bidirectional context to understand text (ideal for classification, search).
- **GPT (Decoder-only):** Uses autoregressive next-token prediction to generate coherent text (ideal for text generation).

## Multimodal Models
CLIP bridges the semantic gap between vision and language by matching text embeddings with image embeddings using a shared contrastive latent space.
"""
    },
    {
        "filename": "day-14-rag-pipelines.md",
        "title": "Context Management, Prompting & RAG Pipelines",
        "day": 14,
        "date": "2024-03-22",
        "module": "Generative AI and Foundation Models",
        "pdfUrl": "/notes/genai-day14.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/genai-rag",
        "topics": ["Prompt Design", "Vector Databases", "RAG Pipeline", "Fine-Tuning"],
        "content": """# Context Management, Prompting & RAG Pipelines

Foundation models have static knowledge cutoffs and hallucination tendencies. We explore prompt management and dynamic context injection.

## Retrieval-Augmented Generation (RAG)
Instead of expensive retraining, RAG dynamically fetches relevant source documents and feeds them to the LLM as context along with the user's query.

```mermaid
graph TD
    Query[User Query] --> Embeddings[Embedding Model]
    Embeddings --> VectorDB[(Vector DB Search)]
    VectorDB --> Context[Context Retrieval]
    Context --> LLM[LLM Prompt Assembly]
    LLM --> Answer[Accurate, Grounded Answer]
```

## Vector Databases
Vector databases (Chroma, Pinecone, FAISS) index high-dimensional embeddings to perform cosine similarity searches in milliseconds.
"""
    },
    {
        "filename": "day-15-ai-dev-workflows.md",
        "title": "AI-Assisted Workflows & Agentic Environments",
        "day": 15,
        "date": "2024-03-29",
        "module": "AI-Assisted Software Development",
        "pdfUrl": "/notes/aidev-day15.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/ai-assisted-dev",
        "topics": ["Code Generation", "Debugging with LLMs", "Automated Testing", "Agentic Coding"],
        "content": """# AI-Assisted Workflows & Agentic Environments

Software engineering is undergoing a tectonic shift. We study how to leverage LLMs and autonomous agents inside development environments.

## Automated Workflows
From simple tab-completions to complex automated testing, code models leverage structural patterns to autocomplete, generate tests, and refactor files.

## Agentic Coding Systems
Autonomous AI agents can write, test, debug, and compile applications inside isolated sandboxes, performing multi-step loops to fulfill goals.
"""
    },
    {
        "filename": "day-16-frontend-react.md",
        "title": "Modern Front End Architecture & React",
        "day": 16,
        "date": "2024-04-05",
        "module": "Masterclass Series A: Front End Development",
        "pdfUrl": "/notes/frontend-day16.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/frontend-react",
        "topics": ["HTML & CSS Grid", "Asynchronous JS", "React Framework", "Redux/Context State"],
        "content": """# Modern Front End Architecture & React

Web interfaces represent the primary access channel for digital users. We learn to construct premium, responsive React front-ends.

## Responsive Styling & Semantics
Using semantic HTML5 elements alongside modern CSS layouts (Flexbox, Grid) guarantees layout fluidness across devices.

## React State Management
We cover React's reactive render cycle, virtual DOM reconciliations, and state hook flows.

```javascript
import React, { useState, useEffect } from 'react';

function NotesCounter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(count + 1)}>
      Notes Counted: {count}
    </button>
  );
}
```
"""
    },
    {
        "filename": "day-17-backend-architecture.md",
        "title": "Back End Engineering & REST APIs",
        "day": 17,
        "date": "2024-04-12",
        "module": "Masterclass Series B: Back End Development",
        "pdfUrl": "/notes/backend-day17.pdf",
        "material": "https://github.com/ai-ml-iit-mandi/backend-node",
        "topics": ["Node.js Server", "CRUD REST APIs", "JWT Security", "Deployment"],
        "content": """# Back End Engineering & REST APIs

We finalize our technical foundation by constructing high-performance back-ends to store data, secure users, and route API commands.

## RESTful Routing
We map HTTP methods (GET, POST, PUT, DELETE) to specific database actions, establishing strict validation and error handling boundaries.

```javascript
const express = require('express');
const app = express();
app.use(express.json());

app.get('/api/lectures', (req, res) => {
  res.json({ status: "success", data: [] });
});
```

## JWT Authentication & Security
We secure endpoints using JSON Web Tokens (JWT) inside auth headers, preventing unauthorized data breaches.
"""
    }
]

# Write all markdown files
for lecture in lectures_data:
    filepath = os.path.join(lectures_dir, lecture["filename"])
    frontmatter = f"""---
title: "{lecture['title']}"
day: {lecture['day']}
date: "{lecture['date']}"
module: "{lecture['module']}"
pdfUrl: "{lecture['pdfUrl']}"
material: "{lecture['material']}"
topics: {lecture['topics']}
---

"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter + lecture["content"])

print(f"Successfully generated {len(lectures_data)} lecture markdown files in {lectures_dir}.")
