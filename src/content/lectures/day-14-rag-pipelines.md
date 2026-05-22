---
title: "Context Management, Prompting & RAG Pipelines"
day: 14
date: "2024-03-22"
module: "Generative AI and Foundation Models"
pdfUrl: "/notes/genai-day14.pdf"
material: "https://github.com/ai-ml-iit-mandi/genai-rag"
topics: ['Prompt Design', 'Vector Databases', 'RAG Pipeline', 'Fine-Tuning']
---

# Context Management, Prompting & RAG Pipelines

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
