---
title: "AI & ML Paradigms, Feature Extraction & Classification"
day: 0
date: "2024-01-10"
module: "Introduction to AI and Machine Learning"
pdfUrl: "/notes/intro-day0a.pdf"
material: "https://github.com/ai-ml-iit-mandi/ai-ml-foundations"
topics: ['AI vs ML', 'Feature Extraction', 'Curse of Dimensionality', 'Supervised Learning', 'Data Labeling']
---

# AI & ML Paradigms, Feature Extraction & Classification

Welcome to Module 00! Before diving into code, we establish the absolute conceptual and mathematical bedrock of Artificial Intelligence (AI) and Machine Learning (ML).

---

## 1. Artificial Intelligence vs. Machine Learning

*   **Artificial Intelligence (AI):** The overarching field of creating systems capable of mimicking human-like cognitive functions (reasoning, learning, problem-solving). This includes heuristics, rule-based expert systems, and search algorithms.
*   **Machine Learning (ML):** A specific subset of AI where systems *learn from data* without being explicitly programmed. Instead of hardcoded rules, we define an objective and let statistical optimization algorithms determine the optimal parameters.

$$\text{AI} \supset \text{ML} \supset \text{Deep Learning}$$

---

## 2. Feature Extraction & Dimensionality

When presenting raw data (like images or audio) to a machine learning model, we must map raw measurements to structured representations called **features**.

*   **Feature Extraction:** The process of transforming raw, high-dimensional inputs into a lower-dimensional, informative set of numerical features.
*   **Dimensionality ($D$):** The number of features representing each data point. For a data matrix $X \in \mathbb{R}^{N \times D}$, $D$ is the dimensionality.

---

## 3. The Curse of Dimensionality

As the dimensionality $D$ increases, the volume of the space grows exponentially. Consequently:
1.  **Sparsity:** Data points become extremely sparse in high-dimensional space, requiring exponentially more training data to maintain the same density.
2.  **Distance Convergence:** In high dimensions, the distance between any two points (e.g., Euclidean distance) converges to a constant value. Distance-based metrics lose their discriminative power:

$$\lim_{D \to \infty} \frac{\text{dist}_{\max} - \text{dist}_{\min}}{\text{dist}_{\min}} = 0$$

> [!WARNING]
> **Curse of Dimensionality:** Models trained on highly dimensional data with too few samples are extremely prone to overfitting.

---

## 4. Paradigms of Machine Learning

| Paradigm | Objective | Core Mechanism |
| :--- | :--- | :--- |
| **Supervised Learning** | Predict targets for labeled inputs | Learn mapping $f(x) \to y$ |
| **Unsupervised Learning** | Discover hidden structures in unlabeled data | Clustering, Dimensionality Reduction |
| **Reinforcement Learning**| Maximize cumulative reward over time | Agent-Environment feedback loops |

### Supervised Learning Subtypes
1.  **Classification:** Predicting a discrete, categorical label ($y \in \{0, 1\}$ or $\{1, \dots, K\}$).
2.  **Regression:** Predicting a continuous numerical value ($y \in \mathbb{R}$).

---

## 5. Data Labels & Types of Classification

Data labels $y$ determine the classification task:
*   **Categorical / Discrete Labels:** Represent distinct classes (e.g., Cat vs. Dog, Spam vs. Ham).
*   **Classification Objectives:**
    *   **Binary Classification:** Exactly two classes (e.g., Class $0$ and Class $1$).
    *   **Multi-class Classification:** More than two mutually exclusive classes (e.g., digit recognition $0-9$).
    *   **Multi-label Classification:** A single sample can belong to multiple classes simultaneously.

---

## 6. Model Validation & Splitting

To ensure our models generalize to unseen real-world scenarios, we split our labeled dataset into:
*   **Training Data:** Used by optimization algorithms to fit the model parameters (weights $w$ and bias $b$).
*   **Testing Data:** Held out completely during training and used strictly for final validation and evaluation.
