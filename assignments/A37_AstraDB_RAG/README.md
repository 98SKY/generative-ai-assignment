# Assignment 37: AstraDB RAG

## Objective

Build a scalable Retrieval Augmented Generation (RAG) system using AstraDB as a cloud vector database.

---

## Tasks Completed

### Task 1

Created AstraDB Vector Database.

### Task 2

Connected LangChain with AstraDB.

### Task 3

Loaded and chunked PDF documents.

### Task 4

Generated embeddings and stored vectors.

### Task 5

Built PDF Question Answering RAG pipeline.

### Task 6

Validated answers using document content.

---

## Architecture

PDF

↓

Text Splitter

↓

Embeddings

↓

AstraDB Vector Store

↓

Retriever

↓

Groq LLM

↓

Answer

---

## Observations & Insights

### 1. Why AstraDB is useful for Production RAG

* Fully managed cloud database
* Highly scalable
* Persistent storage
* Easy integration with LangChain

### 2. Importance of Session State in GenAI Apps

* Maintains conversation history
* Improves contextual responses
* Enables conversational experiences

### 3. Difference Between FAISS and AstraDB

| FAISS                     | AstraDB             |
| ------------------------- | ------------------- |
| Local storage             | Cloud storage       |
| Not distributed           | Distributed         |
| No persistence by default | Persistent          |
| Best for development      | Best for production |

---

## Run Order

1. task2_connect_astradb.py
2. task3_load_pdf.py
3. task4_store_embeddings.py
4. task5_rag_application.py
