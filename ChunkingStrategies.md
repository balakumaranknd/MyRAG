## 📚 Chunking Strategies in RAG Systems

Chunking is the process of splitting large documents into smaller pieces before embedding and storing in a vector database.
The choice of strategy directly affects **retrieval quality, cost, latency, and hallucination risk**.

---

# 1️⃣ Fixed-Size (Character-Based) Chunking

### 🔹 Strategy

Split text purely based on character count.

### 🔹 Example

```python
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_text(long_text)
```

### 🔹 Use Cases

* Quick prototyping
* Small datasets
* When structure is not important

### ❌ Limitations

* Breaks sentences mid-way
* Poor semantic coherence
* Weak embeddings
* Higher hallucination risk

---

# 2️⃣ Recursive Character Chunking

### 🔹 Strategy

Attempts hierarchical splitting:

```
Paragraph → Line → Sentence → Word → Character
```

### 🔹 Example

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)
```

### 🔹 Use Cases

* General-purpose RAG
* PDFs, blog posts, documentation
* Balanced retrieval systems

### ❌ Limitations

* Still size-based, not meaning-aware
* Requires tuning chunk size
* Overlap increases embedding cost
* Cannot detect conceptual boundaries

---

# 3️⃣ Markdown Header-Based Chunking

### 🔹 Strategy

Split based on Markdown headers (`#`, `##`, etc.)

### 🔹 Example

```python
from langchain_text_splitters import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
chunks = splitter.split_text(markdown_text)
```

### 🔹 Use Cases

* Structured documentation
* Knowledge bases
* Course materials

### ❌ Limitations

* Requires clean markdown formatting
* Uneven chunk sizes
* Not suitable for raw PDFs

---

# 4️⃣ Language-Aware Chunking (Code-Aware)

### 🔹 Strategy

Split based on programming language structure (e.g., `class`, `def` in Python).

### 🔹 Example

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import Language

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=400,
    chunk_overlap=50
)

chunks = splitter.split_text(python_code)
```

### 🔹 Use Cases

* Code RAG systems
* Technical documentation
* API reference retrieval

### ❌ Limitations

* Large functions still get split
* Does not understand logical dependencies
* Language-specific only

---

# 5️⃣ Sentence-Based Chunking

### 🔹 Strategy

Split using NLP sentence tokenization.

### 🔹 Example

```python
import nltk
from nltk.tokenize import sent_tokenize

sentences = sent_tokenize(long_text)
```

### 🔹 Use Cases

* FAQ systems
* Legal clauses
* Structured writing

### ❌ Limitations

* Context fragmentation
* Multi-sentence ideas get split
* Too granular for technical docs

---

# 6️⃣ Token-Based Chunking

### 🔹 Strategy

Split based on token count instead of characters.

### 🔹 Example

```python
from langchain_text_splitters import TokenTextSplitter

splitter = TokenTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_text(long_text)
```

### 🔹 Use Cases

* OpenAI API optimization
* Strict context window management
* Cost-sensitive applications

### ❌ Limitations

* Ignores semantic boundaries
* Tokenization varies by model
* Harder to reason about manually

---

# 7️⃣ Semantic Chunking (Embedding-Based)

### 🔹 Strategy

Split when embedding similarity drops significantly.

### 🔹 Conceptual Example

1. Generate sentence embeddings
2. Compute similarity between consecutive sentences
3. Split when similarity < threshold

### 🔹 Use Cases

* High-quality enterprise RAG
* Research systems
* Long-form documents

### ❌ Limitations

* Computationally expensive
* Slower ingestion pipeline
* Complex implementation
* Overkill for small datasets

---

# 8️⃣ Sliding Window Chunking

### 🔹 Strategy

Create overlapping moving windows across text.

### 🔹 Example

```
Chunk 1: 0–1000
Chunk 2: 800–1800
Chunk 3: 1600–2600
```

### 🔹 Use Cases

* QA systems
* Dense retrieval tasks
* When context continuity is critical

### ❌ Limitations

* Duplicate embeddings
* Higher storage cost
* Slower retrieval

---

# 9️⃣ Hierarchical Chunking

### 🔹 Strategy

Create multi-level chunks:

* Small chunks for retrieval
* Large chunks for answer synthesis

### 🔹 Use Cases

* Enterprise search systems
* Multi-hop QA
* Knowledge graphs

### ❌ Limitations

* Complex indexing
* Requires careful orchestration
* Higher engineering overhead

---

# 📊 Summary Comparison

| Strategy       | Best For           | Main Limitation       |
| -------------- | ------------------ | --------------------- |
| Fixed-size     | Prototyping        | Breaks semantics      |
| Recursive      | General RAG        | Size-driven           |
| Markdown       | Structured docs    | Formatting dependent  |
| Language-aware | Code               | No logical awareness  |
| Sentence       | FAQ/Legal          | Context fragmentation |
| Token-based    | Cost control       | Semantic ignorance    |
| Semantic       | High-quality RAG   | Expensive             |
| Sliding Window | Context continuity | Duplication cost      |
| Hierarchical   | Enterprise systems | Complex setup         |

---

# 🎯 Choosing the Right Strategy

| Scenario                  | Recommended Strategy    |
| ------------------------- | ----------------------- |
| AI Tutor (JSON questions) | No chunking             |
| Theory Notes              | Recursive (800/150)     |
| Code Repository RAG       | Language-aware          |
| Cost-sensitive app        | Token-based             |
| Research-grade system     | Semantic + Hierarchical |

---

## 🚀 Key Insight

Most RAG failures are not LLM problems —
they are **chunking design problems**.

Proper chunking improves:

* Retrieval precision
* Context coherence
* Cost efficiency
* Response accuracy


# CLAUDE
Here are all the text splitting types in LangChain:

---

### 1. Character Splitting
Splits on a single character (e.g. `\n`, `.`, ` `). Simple and fast but can break sentences mid-way.

---

### 2. Recursive Character Splitting
Tries a list of separators in order (`\n\n` → `\n` → `.` → `" "` → `""`) until chunks are small enough. Most commonly used — produces natural, coherent chunks.

---

### 3. Token Splitting
Splits based on token count rather than character count. Important for LLMs because they have token limits, not character limits.

---

### 4. Markdown Header Splitting
Splits based on markdown headers (`#`, `##`, `###`). Preserves document structure and adds header info to metadata.

---

### 5. HTML Header Splitting
Splits based on HTML header tags (`h1`, `h2`, `h3`). Useful for web content and HTML documents.

---

### 6. Code Splitting
Language-aware splitting for source code. Understands syntax boundaries for Python, JavaScript, HTML, SQL, and more.

---

### 7. Semantic Splitting
Uses embeddings to split text at points where the **meaning changes** rather than at fixed character counts. Most intelligent splitter — produces semantically coherent chunks but slower and requires an embedding model.

---

### 8. JSON Splitting
Splits JSON data while respecting the nested structure. Keeps related JSON keys together rather than splitting mid-object.

---

### 9. Sentence Transformers Token Splitting
Similar to token splitting but uses sentence transformer tokenisers specifically. Useful when using sentence transformer embedding models.

---

### Quick Comparison

| Splitter | Splits By | Best For |
|---|---|---|
| Character | Single character | Simple, known separators |
| Recursive Character | Multiple characters in order | General purpose documents |
| Token | Token count | LLM context window management |
| Markdown Header | `#` headers | Markdown files |
| HTML Header | `h1/h2/h3` tags | HTML and web content |
| Code | Language syntax | Source code files |
| Semantic | Meaning change | High quality semantic retrieval |
| JSON | JSON structure | API responses, JSON data |
| Sentence Transformers | Transformer tokens | Sentence transformer models |

Would you like code examples for any specific one?