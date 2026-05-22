---
title: "Gradient Descent, Mathematical Neuron & Parametric Spaces"
day: 0
date: "2024-01-12"
module: "Introduction to AI and Machine Learning"
pdfUrl: "/notes/intro-day0b.pdf"
material: "https://github.com/ai-ml-iit-mandi/gradient-descent-neuron"
topics: ['Gradient Descent', 'Mathematical Neuron', 'Loss Function', 'Parametric Space', 'Binary Classification']
---

# Gradient Descent, Mathematical Neuron & Parametric Spaces

In this lecture, we build our first mathematical model of a **neuron** and learn how to optimize its parameters using **Gradient Descent**.

---

## 1. The Mathematical Neuron

A mathematical neuron mimics a biological neuron by taking a vector of inputs $X = [x_1, x_2, \dots, x_D]^T$, scaling them by weights $W = [w_1, w_2, \dots, w_D]^T$, adding a bias $b$, and applying an activation function.

The linear core of the neuron is the equation of a line (or hyperplane in higher dimensions):

$$f(X) = W^T X + b = \sum_{i=1}^D w_i x_i + b$$

### The Classification Boundary
This line acts as the classification boundary:
*   Points on one side of the line: $W^T X + b > 0 \implies \text{Class } 1$
*   Points on the other side of the line: $W^T X + b < 0 \implies \text{Class } 0$
*   The boundary itself: $W^T X + b = 0$

---

## 2. Neuron as a Discrete Function

To make a discrete classification decision, we apply a step function $\sigma(z)$ (like the Heaviside step function) to the linear output:

$$\hat{y} = \sigma(W^T X + b) = \begin{cases} 1 & \text{if } W^T X + b \ge 0 \\ 0 & \text{if } W^T X + b < 0 \end{cases}$$

### Mathematical Working
1.  **Weighted Summation:** The inputs are scaled by $w_i$, determining the importance/weight of each input feature.
2.  **Thresholding:** The bias $b$ shifts the boundary. If the net signal exceeds the threshold, the neuron fires ($\hat{y} = 1$).

---

## 3. Data Space vs. Parametric Space

Understanding the duality between Data Space and Parametric (Weight) Space is critical for visualization.

| Space | Dimension | Representation of a Data Point $(X, y)$ | Representation of a Model (Weights $W$, Bias $b$) |
| :--- | :--- | :--- | :--- |
| **Data Space** | $D$ (Feature count) | A single point $(x_1, \dots, x_D)$ in space | A line/hyperplane separating the points ($W^T X + b = 0$) |
| **Parametric Space** | $D+1$ (Weights + Bias) | A linear constraint line or boundary region | A single point $(w_1, \dots, w_D, b)$ representing the model |

$$\text{Data Space point: } X_i \iff \text{Parametric Space boundary constraint: } W^T X_i + b = 0$$

---

## 4. How Gradient Descent Works

Optimization is the process of finding weights $W$ and bias $b$ that minimize a **Loss Function** $L(W, b)$.

### Loss Function
The Loss Function measures the error between the predicted values $\hat{y}_i$ and the true labels $y_i$. For continuous mathematical optimization, we require differentiable loss functions (e.g., Mean Squared Error or Cross-Entropy).

### Minimizing the Loss using Derivatives
The derivative (gradient) of a function points in the direction of the steepest ascent. To minimize the loss, we calculate the partial derivatives and update parameters in the *opposite* direction:

$$W \leftarrow W - \eta \frac{\partial L}{\partial W}$$
$$b \leftarrow b - \eta \frac{\partial L}{\partial b}$$

Where $\eta$ (eta) represents the **learning rate**—a scalar controlling the step size of each iteration.

```python
# One iteration of Gradient Descent parameter updates
w_gradient = calculate_gradient_w(X, y, w, b)
b_gradient = calculate_gradient_b(X, y, w, b)

w = w - learning_rate * w_gradient
b = b - learning_rate * b_gradient
```

---

## 5. Feature Extraction vs. Classification Loss

*   **Feature Extraction:** Focuses on representation learning, transforming raw inputs to separate classes or extract invariant information.
*   **Classification:** Maps extracted features directly to decision labels.
*   **Loss Dependency:** The final system performance is dependent on both! If feature extraction fails to make the data linearly separable, no linear neuron classifier can achieve zero loss.

---

## 6. Binary Classification & One-Hot Labeling

*   **Binary Classification:** Classification where the label belongs to one of two categories. Usually represented as $y \in \{0, 1\}$ or $y \in \{-1, +1\}$.
*   **One-Hot Labeling:** A method of encoding categorical variables as binary vectors. For $K$ classes, a label is represented as a vector of length $K$ with a $1$ at the index of the class and $0$ elsewhere.
    *   Example for three classes (Cat, Dog, Bird):
        *   $\text{Cat} = [1, 0, 0]^T$
        *   $\text{Dog} = [0, 1, 0]^T$
        *   $\text{Bird} = [0, 0, 1]^T$
*   This approach avoids implying an ordinal relationship between categorical features or labels.
