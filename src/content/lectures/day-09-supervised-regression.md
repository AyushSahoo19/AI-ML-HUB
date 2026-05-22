---
title: "Supervised Learning & Regression Models"
day: 9
date: "2024-02-22"
module: "Fundamentals of Classical Machine Learning"
pdfUrl: "/notes/ml-day9.pdf"
material: "https://github.com/ai-ml-iit-mandi/ml-regression"
topics: ['Supervised Learning', 'Linear Regression', 'Gradient Descent', 'Evaluation Metrics']
---

# Supervised Learning & Regression Models

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
