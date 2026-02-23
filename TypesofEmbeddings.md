## 1. Text Embeddings

| Embedding Type               | Description                                           | Example Models                           | Primary Use Case        |
| ---------------------------- | ----------------------------------------------------- | ---------------------------------------- | ----------------------- |
| General Semantic Embeddings  | Capture overall meaning of text                       | OpenAI `text-embedding-3-large`, BGE, E5 | RAG document retrieval  |
| Sentence Embeddings          | Optimized for sentence-level similarity               | SBERT                                    | Semantic search         |
| Instruction-Tuned Embeddings | Trained with query/document distinction               | E5, Instructor                           | Query-aware RAG         |
| Domain-Specific Embeddings   | Trained on specific domains (legal, medical, finance) | BioBERT, FinBERT                         | Industry-specific RAG   |
| Multilingual Embeddings      | Support multiple languages                            | LaBSE, multilingual-e5                   | Cross-lingual retrieval |

## 2. Code Embeddings

| Embedding Type              | Description                       | Example Models            | Primary Use Case    |
| --------------------------- | --------------------------------- | ------------------------- | ------------------- |
| Code Semantic Embeddings    | Understand code logic & structure | CodeBERT                  | Code search         |
| Docstring-Code Embeddings   | Map code ↔ documentation          | OpenAI code models        | Developer assistant |
| Repository-Level Embeddings | Entire repo understanding         | DeepSeek-Coder embeddings | Codebase RAG        |


## 3. Image Embeddings

| Embedding Type        | Description                        | Example Models | Primary Use Case  |
| --------------------- | ---------------------------------- | -------------- | ----------------- |
| Vision Embeddings     | Convert images into vectors        | CLIP           | Image similarity  |
| Multimodal Embeddings | Align text and image in same space | CLIP, BLIP     | Image-text search |
| Face Embeddings       | Encode facial features             | FaceNet        | Face recognition  |


## 4. Audio Embeddings

| Embedding Type                 | Description                       | Example Models           | Primary Use Case     |
| ------------------------------ | --------------------------------- | ------------------------ | -------------------- |
| Speech Embeddings              | Capture speech characteristics    | Wav2Vec                  | Speaker recognition  |
| Audio Event Embeddings         | Detect audio patterns             | YAMNet                   | Sound classification |
| Transcription-Based Embeddings | Convert speech → text → embedding | Whisper + text embedding | Audio RAG            |


## 5. Video Embeddings

| Embedding Type              | Description                  | Example Models         | Primary Use Case    |
| --------------------------- | ---------------------------- | ---------------------- | ------------------- |
| Frame-Based Embeddings      | Extract embeddings per frame | ResNet + pooling       | Video similarity    |
| Temporal Video Embeddings   | Capture motion over time     | TimeSformer            | Video understanding |
| Multimodal Video Embeddings | Align video + text           | CLIP-like video models | Video search        |


## 6. Graph Embeddings

| Embedding Type                  | Description                 | Example Models | Primary Use Case       |
| ------------------------------- | --------------------------- | -------------- | ---------------------- |
| Node Embeddings                 | Represent graph nodes       | Node2Vec       | Recommendation systems |
| Knowledge Graph Embeddings      | Encode entity relationships | TransE         | Knowledge retrieval    |
| Graph Neural Network Embeddings | Learned via GNN             | GraphSAGE      | Fraud detection        |


## 7. Structured Data Embeddings

| Embedding Type                      | Description               | Example Models    | Primary Use Case  |
| ----------------------------------- | ------------------------- | ----------------- | ----------------- |
| Tabular Embeddings                  | Represent structured rows | TabTransformer    | Structured RAG    |
| Categorical Embeddings              | Encode categories         | Entity embeddings | ML models         |
| Hybrid Structured + Text Embeddings | Combine metadata + text   | Custom pipelines  | Enterprise search |


## 8. Sparse Vs Dense Embeddings

| Type              | Description                    | Example                | Use Case          |
| ----------------- | ------------------------------ | ---------------------- | ----------------- |
| Sparse Embeddings | High dimensional, mostly zeros | BM25, TF-IDF           | Keyword search    |
| Dense Embeddings  | Compact dense vectors          | OpenAI, BGE            | Semantic search   |
| Hybrid Retrieval  | Combine sparse + dense         | Pinecone hybrid search | High-accuracy RAG |


## Which type to Use in RAG?

| RAG Type              | Recommended Embedding        |
| --------------------- | ---------------------------- |
| General Knowledge RAG | General semantic embeddings  |
| Academic RAG          | Instruction-tuned embeddings |
| Multilingual RAG      | Multilingual embeddings      |
| Code RAG              | Code embeddings              |
| Enterprise Search     | Hybrid (dense + sparse)      |
| Medical / Legal       | Domain-specific embeddings   |

## Next
✅ Compare OpenAI vs BGE vs E5 embeddings

✅ Explain embedding dimensions and performance trade-offs

✅ Show how to benchmark embeddings

✅ Explain cosine similarity vs dot product

✅ Explain chunk size vs embedding quality