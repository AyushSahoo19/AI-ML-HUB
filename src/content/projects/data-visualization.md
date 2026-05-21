---
title: "data-visualization"
description: "Interactive data exploration, cleaning, and custom plotting pipelines. Contains helper modules for automated EDA, outliers detection, and custom styling filters."
language: "Jupyter Notebook"
stars: 15
forks: 4
lastUpdated: "5 hours ago"
files:
  - path: "src/plotter.py"
    language: "python"
    content: |
      import matplotlib.pyplot as plt
      import seaborn as sns
      import numpy as np

      def apply_brutalist_theme():
          """
          Applies a custom brutalist, high-contrast, chunky plotting style
          similar to the neo-brutalist theme of our web app!
          """
          plt.rcParams['figure.facecolor'] = '#ffffff'
          plt.rcParams['axes.facecolor'] = '#ffffff'
          plt.rcParams['axes.edgecolor'] = '#000000'
          plt.rcParams['axes.linewidth'] = 3.0
          plt.rcParams['grid.color'] = '#000000'
          plt.rcParams['grid.linestyle'] = '--'
          plt.rcParams['grid.linewidth'] = 1.0
          plt.rcParams['font.weight'] = 'bold'
          plt.rcParams['axes.labelweight'] = 'bold'
          plt.rcParams['axes.titleweight'] = 'bold'
          plt.rcParams['xtick.major.width'] = 2.0
          plt.rcParams['ytick.major.width'] = 2.0
          
      def plot_decision_boundary(model, X, y, title="Decision Boundary"):
          apply_brutalist_theme()
          fig, ax = plt.subplots(figsize=(8, 6))
          
          # Create meshgrid
          h = .02
          x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
          y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
          xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
          
          # Predict decision boundary
          Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
          Z = Z.reshape(xx.shape)
          
          # Brutalist flat contour lines
          ax.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.3)
          
          # Scatter classes
          ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral, edgecolors='black', linewidths=1.5, s=60)
          ax.set_title(title, fontsize=14, pad=15)
          ax.grid(True)
          return fig
  - path: "src/analyzer.py"
    language: "python"
    content: |
      import pandas as pd
      import numpy as np

      class AutoEDA:
          def __init__(self, filepath):
              self.df = pd.read_csv(filepath)
              
          def get_summary(self):
              """
              Computes core EDA stats: shapes, missing numbers, and datatypes.
              """
              summary = {
                  "shape": self.df.shape,
                  "missing_values": self.df.isnull().sum().to_dict(),
                  "dtypes": self.df.dtypes.astype(str).to_dict()
              }
              return summary

          def detect_outliers_iqr(self, column):
              """
              Detects outliers using the Interquartile Range (IQR) method.
              """
              q1 = self.df[column].quantile(0.25)
              q3 = self.df[column].quantile(0.75)
              iqr = q3 - q1
              lower_bound = q1 - 1.5 * iqr
              upper_bound = q3 + 1.5 * iqr
              
              outliers = self.df[(self.df[column] < lower_bound) | (self.df[column] > upper_bound)]
              return outliers
  - path: "data/samples.json"
    language: "json"
    content: |
      [
        {"name": "Iris Dataset", "samples": 150, "features": 4, "type": "classification"},
        {"name": "Boston Housing", "samples": 506, "features": 13, "type": "regression"},
        {"name": "MNIST", "samples": 70000, "features": 784, "type": "classification"}
      ]
---

# `data-visualization` 📊

Welcome to the **data-visualization** project directory! This repository acts as our custom visualization lab, building tailored analytical pipelines and aesthetic graphing components.

## 🌟 Visual Philosophy: Neo-Brutalist Graphing

We believe that charts should not only be informative, but they should also fit the high-contrast aesthetic of modern developer platforms. Rather than generating plain, generic Seaborn plots, this repo wraps Matplotlib to implement:
- **Thick chunky black borders** (`axes.linewidth: 3.0`)
- **Dashed gridlines** overlays
- **Vibrant flat pastel colors** (Spectral, Coral, Yellow)
- **Bold typography hierarchy** for all labels and ticks

## 📦 What's Inside

- **`src/plotter.py`**: Custom Matplotlib theme configurations and flat decision boundary shading algorithms for classification models.
- **`src/analyzer.py`**: An automated Exploratory Data Analysis (EDA) engine. Instantly computes dataset structures, lists column types, and tracks structural outlier vectors using statistical Interquartile Ranges (IQR).
- **`data/samples.json`**: Pre-configured JSON index containing dataset descriptors for classification and regression tasks.

## 🚀 Running the Brutalist Visualizer

You can import our plotter custom theme directly inside your Jupyter notebooks:

```python
import numpy as np
from src.plotter import apply_brutalist_theme, plot_decision_boundary
from src.models import Perceptron  # Assuming from ai-ml-models

# 1. Apply high-contrast theme
apply_brutalist_theme()

# 2. Train perceptron
X = np.array([[1, 2], [2, 3], [3, 1], [4, 3]])
y = np.array([0, 0, 1, 1])
model = Perceptron()
model.fit(X, y)

# 3. Render decision boundaries
fig = plot_decision_boundary(model, X, y, title="Brutalist Decision Boundary")
fig.show()
```

## 🛠️ Issues & Feedback
If you have suggestions for new plotting styles (e.g. glassmorphism elements or D3 integrations), open an issue in the tab above!
