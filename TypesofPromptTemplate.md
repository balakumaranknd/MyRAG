# LangChain Prompt Templates — Methods & Use Cases

---

## 1. PromptTemplate.from_template

**Use case:** Simple single turn prompts with one or more variables. Quickest way to create a prompt.

```python
from langchain_core.prompts import PromptTemplate

pt = PromptTemplate.from_template("Answer this question: {question}")

print(pt.format(question="What is RAG?"))
# Answer this question: What is RAG?
```

---

## 2. PromptTemplate (explicit)

**Use case:** When you want strict validation of input variables. Raises an error if variables are missing or mismatched.

```python
from langchain_core.prompts import PromptTemplate

pt = PromptTemplate(
    input_variables=["context", "question"],
    template="Context: {context}\nQuestion: {question}"
)

print(pt.format(context="RAG is a retrieval method.", question="What is RAG?"))
```

---

## 3. PromptTemplate.from_file

**Use case:** Load a prompt from an external `.txt` file. Useful when you want to manage prompts outside your codebase.

```
# prompt.txt
Answer the following question using the context.
Context: {context}
Question: {question}
```

```python
from langchain_core.prompts import PromptTemplate

pt = PromptTemplate.from_file("prompt.txt")
print(pt.format(context="RAG stands for Retrieval Augmented Generation.", question="What is RAG?"))
```

---

## 4. ChatPromptTemplate.from_template

**Use case:** Quick single human message prompt for chat models. No system message, minimal setup.

```python
from langchain_core.prompts import ChatPromptTemplate

ct = ChatPromptTemplate.from_template("Answer this: {question}")

print(ct.format_messages(question="What is RAG?"))
```

---

## 5. ChatPromptTemplate.from_messages

**Use case:** Full control over system, human, and AI messages. Best for RAG pipelines and chat models that need a persona or strict instructions.

```python
from langchain_core.prompts import ChatPromptTemplate

ct = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant specialised in {topic}."),
    ("human", "Context: {context}\nQuestion: {question}")
])

print(ct.format_messages(
    topic="machine learning",
    context="RAG combines retrieval with generation.",
    question="What is RAG?"
))
```

---

## 6. ChatPromptTemplate with conversation history

**Use case:** Multi-turn conversations where previous messages are included. Used in chatbots to maintain context across turns.

```python
from langchain_core.prompts import ChatPromptTemplate

ct = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}"),
    ("ai", "{answer}"),
    ("human", "{followup}")
])
```

---

## 7. MessagesPlaceholder

**Use case:** Dynamically insert a list of chat messages into a prompt. Essential for chatbots with memory — the full chat history is injected at runtime.

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

ct = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),  # history injected here
    ("human", "{question}")
])
```

---

## 8. FewShotPromptTemplate

**Use case:** Provide worked examples before the actual question to guide the model's output format or style.

```python
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {"question": "What is RAG?",   "answer": "Retrieval Augmented Generation"},
    {"question": "What is FAISS?", "answer": "A vector similarity search library by Facebook"}
]

example_prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template="Question: {question}\nAnswer: {answer}"
)

few_shot = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Answer questions like the examples below:",
    suffix="Question: {question}\nAnswer:",
    input_variables=["question"]
)

print(few_shot.format(question="What is LangChain?"))
```

---

## 9. FewShotChatMessagePromptTemplate

**Use case:** Few shot examples specifically for chat models. Formats examples as human/AI message pairs.

```python
from langchain_core.prompts import FewShotChatMessagePromptTemplate, ChatPromptTemplate

examples = [
    {"input": "What is RAG?",   "output": "Retrieval Augmented Generation"},
    {"input": "What is FAISS?", "output": "A vector similarity search library"}
]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}")
])

few_shot = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt
)

final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    few_shot,
    ("human", "{question}")
])
```

---

## 10. PipelinePromptTemplate

**Use case:** Compose multiple sub-prompts into one final prompt. Useful when you have reusable prompt components you want to combine.

```python
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts.pipeline import PipelinePromptTemplate

intro_prompt = PromptTemplate.from_template("You are an expert in {topic}.")
question_prompt = PromptTemplate.from_template("{intro}\nAnswer this: {question}")

pipeline_prompt = PipelinePromptTemplate(
    final_prompt=question_prompt,
    pipeline_prompts=[("intro", intro_prompt)]
)

print(pipeline_prompt.format(topic="machine learning", question="What is RAG?"))
```

---

## Quick Decision Guide

| Situation | Use |
|---|---|
| Simple question answer | `PromptTemplate.from_template` |
| Strict variable validation | `PromptTemplate(template=..., input_variables=[...])` |
| Prompt stored in a file | `PromptTemplate.from_file` |
| Chat model, no system message | `ChatPromptTemplate.from_template` |
| Chat model with system message | `ChatPromptTemplate.from_messages` |
| Chatbot with memory | `ChatPromptTemplate.from_messages` + `MessagesPlaceholder` |
| Guide output with examples (non-chat) | `FewShotPromptTemplate` |
| Guide output with examples (chat) | `FewShotChatMessagePromptTemplate` |
| Reusable composed prompts | `PipelinePromptTemplate` |
| RAG pipeline | `ChatPromptTemplate.from_messages` with system + human |