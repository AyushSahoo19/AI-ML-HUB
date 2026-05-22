---
title: "Ensemble Methods & Unsupervised Learning"
day: 10
date: "2024-02-26"
module: "Fundamentals of Classical Machine Learning"
pdfUrl: "/notes/ml-day10.pdf"
material: "https://github.com/ai-ml-iit-mandi/ml-advanced"
topics: ['Decision Trees', 'Random Forests', 'K-Means Clustering', 'PCA Dimensionality']
---

# Ensemble Methods & Unsupervised Learning

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
