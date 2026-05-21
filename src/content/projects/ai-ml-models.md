---
title: "ai-ml-models"
description: "From-scratch implementations of foundational ML models using only NumPy and basic Python. Includes Linear Regression, Perceptron, Custom Optimizers, and Evaluation Metrics."
language: "Python"
stars: 42
forks: 12
lastUpdated: "2 hours ago"
files:
  - path: "src/models/linear_regression.py"
    language: "python"
    content: |
      import numpy as np

      class LinearRegression:
          def __init__(self, learning_rate=0.01, epochs=1000):
              self.lr = learning_rate
              self.epochs = epochs
              self.weights = None
              self.bias = None

          def fit(self, X, y):
              n_samples, n_features = X.shape
              self.weights = np.zeros(n_features)
              self.bias = 0.0

              for _ in range(self.epochs):
                  # Forward pass (y = wx + b)
                  y_predicted = np.dot(X, self.weights) + self.bias
                  
                  # Compute gradients
                  dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
                  db = (1 / n_samples) * np.sum(y_predicted - y)

                  # Update parameters
                  self.weights -= self.lr * dw
                  self.bias -= self.lr * db

          def predict(self, X):
              return np.dot(X, self.weights) + self.bias
  - path: "src/models/perceptron.py"
    language: "python"
    content: |
      import numpy as np

      class Perceptron:
          def __init__(self, learning_rate=0.01, epochs=100):
              self.lr = learning_rate
              self.epochs = epochs
              self.weights = None
              self.bias = None

          def fit(self, X, y):
              n_samples, n_features = X.shape
              self.weights = np.zeros(n_features)
              self.bias = 0.0

              # Map labels to -1 or 1
              y_ = np.where(y <= 0, -1, 1)

              for _ in range(self.epochs):
                  for idx, x_i in enumerate(X):
                      linear_output = np.dot(x_i, self.weights) + self.bias
                      y_predicted = np.sign(linear_output)
                      
                      # Perceptron update rule: w = w + lr * y_i * x_i
                      update = self.lr * (y_[idx] - y_predicted)
                      self.weights += update * x_i
                      self.bias += update

          def predict(self, X):
              linear_output = np.dot(X, self.weights) + self.bias
              return np.where(linear_output >= 0, 1, 0)
  - path: "src/optimizers/gd.py"
    language: "python"
    content: |
      # Standard Mini-batch Gradient Descent Optimizer from Scratch
      import numpy as np

      class GradientDescent:
          def __init__(self, lr=0.01, batch_size=32):
              self.lr = lr
              self.batch_size = batch_size

          def update(self, params, grads):
              """
              Performs a simple gradient update step.
              params: list of np.ndarray
              grads: list of np.ndarray
              """
              updated_params = []
              for p, g in zip(params, grads):
                  p_new = p - self.lr * g
                  updated_params.append(p_new)
              return updated_params
  - path: "src/utils/metrics.py"
    language: "python"
    content: |
      import numpy as np

      def mean_squared_error(y_true, y_pred):
          return np.mean((y_true - y_pred) ** 2)

      def accuracy_score(y_true, y_pred):
          return np.sum(y_true == y_pred) / len(y_true)

      def r2_score(y_true, y_pred):
          ssr = np.sum((y_true - y_pred) ** 2)
          sst = np.sum((y_true - np.mean(y_true)) ** 2)
          return 1 - (ssr / sst)
  - path: "data/train.csv"
    language: "csv"
    content: |
      feature_1,feature_2,target
      0.82,-0.12,1.64
      -0.45,0.92,0.47
      1.22,1.15,3.37
      -0.90,-0.84,-2.58
      0.15,0.03,0.33
---

# `ai-ml-models` 🚀

Welcome to the **ai-ml-models** repository! This project contains foundational machine learning models constructed from scratch using only core Python and NumPy.

The primary objective of this library is **educational clarity**. By bypassing frameworks like Scikit-Learn or PyTorch, we can unpack the internal mathematics and gradient calculations directly in clean vectorised code.

## 🛠️ Included Models & Tools

- **Linear Regression**: A standard gradient descent optimizer resolving $y = \mathbf{w}^T\mathbf{x} + b$ with mean squared error gradient calculations.
- **Perceptron**: The original single-layer binary classifier using the classic Perceptron update rule.
- **Gradient Descent Optimizer**: A generalized batch gradient step updater.
- **Metrics Utilities**: Hand-rolled mean squared error (MSE), classification accuracy, and $R^2$ determination.

## 📈 Mathematics Covered

### 1. Linear Regression Gradients
The Mean Squared Error loss is:
$$J(w, b) = \frac{1}{2N} \sum_{i=1}^{N} (y_i - (\mathbf{w}^T \mathbf{x}_i + b))^2$$

The gradient equations implemented in our solver are:
$$\frac{\partial J}{\partial \mathbf{w}} = \frac{1}{N} \mathbf{X}^T (\mathbf{\hat{y}} - \mathbf{y})$$
$$\frac{\partial J}{\partial b} = \frac{1}{N} \sum (\mathbf{\hat{y}} - \mathbf{y})$$

### 2. Perceptron Convergence
For any misclassified sample $i$ where $y_i(\mathbf{w}^T\mathbf{x}_i + b) \le 0$:
$$\mathbf{w} \leftarrow \mathbf{w} + \eta y_i \mathbf{x}_i$$
$$b \leftarrow b + \eta y_i$$

## 🚀 Quick Start

To use the model in your own local Jupyter environment:

```python
import numpy as np
from src.models.linear_regression import LinearRegression
from src.utils.metrics import r2_score

# Create synthetic data
X = np.random.randn(100, 2)
true_w = np.array([2.5, -1.2])
y = np.dot(X, true_w) + 0.5 + np.random.normal(0, 0.1, 100)

# Instantiate and fit
model = LinearRegression(learning_rate=0.05, epochs=500)
model.fit(X, y)

# Predict and evaluate
predictions = model.predict(X)
print("R2 Score:", r2_score(y, predictions))
```

## 📬 Contributing & Issues
Spotted a bug in our gradient derivations or want to submit an optimization like Adam or AdaGrad? Open a Pull Request or create an Issue in the tabs above!
