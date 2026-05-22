---
title: "CNNs, LSTMs & Transformer Basics"
day: 12
date: "2024-03-10"
module: "Fundamentals of Deep Learning"
pdfUrl: "/notes/dl-day12.pdf"
material: "https://github.com/ai-ml-iit-mandi/dl-cnn"
topics: ['CNNs for Vision', 'LSTMs & RNNs', 'Self-Attention', 'Deep Architectures']
---

# CNNs, LSTMs & Transformer Basics

Standard MLPs struggle with spatial images and sequential text. We study structural neural architectures.

## Convolutional Neural Networks (CNNs)
CNNs utilize overlapping kernel filters to capture local spatial details (edges, shapes) across input images, maintaining translation invariance.

## Recurrent Networks & Transformers
- **RNNs & LSTMs:** Maintain sequential memory cells to process sequences (time-series, texts), but suffer from vanishing gradients.
- **Transformers:** Resolve sequential bottlenecks by executing a **Self-Attention** matrix, computing relationships across all inputs simultaneously.
