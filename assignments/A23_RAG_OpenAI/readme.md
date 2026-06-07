# Assignment 23: OpenAI & Retrieval-Augmented Generation (RAG)

## Overview

This project demonstrates the fundamentals of Retrieval-Augmented Generation (RAG) using LangChain, Embedding Models, Retrievers, and Vector Stores.

The goal is to enhance Large Language Models (LLMs) with external knowledge sources, allowing them to answer questions based on retrieved information rather than relying solely on training data.

---

## Objectives

* Understand OpenAI and Retrieval-Augmented Generation (RAG)
* Retrieve information from Wikipedia
* Build vector store retrievers using embeddings
* Explore advanced retrieval strategies
* Load and process YouTube transcripts
* Build a YouTube Content RAG Chatbot
* Compare different retrieval approaches

---

## Project Structure

```text
A23_OpenAI_RAG/
│
├── task1_openai_setup.py
├── task2_wikipedia_retriever.py
├── task3_vectorstore_retriever.py
├── task4_mmr_retriever.py
├── task5_multiquery_retriever.py
├── task6_contextual_compression.py
├── task7_youtube_loader.py
├── task8_youtube_vectorstore.py
├── task9_youtube_rag_chatbot.py
├── observations.md
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* LangChain
* OpenAI
* Hugging Face Embeddings
* ChromaDB
* FAISS (Optional)
* Wikipedia Retriever
* YouTube Transcript API

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd A23_OpenAI_RAG
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install langchain
pip install langchain-community
pip install langchain-openai
pip install langchain-chroma
pip install langchain-huggingface

pip install chromadb
pip install sentence-transformers
pip install wikipedia
pip install youtube-transcript-api
```

---

## Tasks Completed

### Task 1 – OpenAI Setup

* Configured OpenAI API Key
* Sent a basic prompt to OpenAI Chat Model
* Generated a response

---

### Task 2 – Wikipedia Retriever

* Retrieved documents from Wikipedia
* Displayed retrieved content and metadata

---

### Task 3 – Vector Store Retriever

* Created embeddings for documents
* Stored embeddings in ChromaDB
* Performed similarity search

---

### Task 4 – MMR Retriever

* Implemented Maximal Marginal Relevance Retrieval
* Compared results with traditional similarity search
* Observed increased diversity in retrieved documents

---

### Task 5 – Multi-Query Retriever

* Generated multiple query variations using LLM
* Improved retrieval coverage
* Reduced chances of missing relevant documents

---

### Task 6 – Contextual Compression Retriever

* Compressed retrieved content
* Removed irrelevant information
* Improved context quality sent to LLM

---

### Task 7 – YouTube Loader

* Loaded transcript from a YouTube video
* Extracted textual content
* Prepared transcript for chunking

---

### Task 8 – YouTube Vector Store

* Split transcript into chunks
* Generated embeddings
* Stored chunks in ChromaDB
* Created retriever

---

### Task 9 – YouTube RAG Chatbot

Features:

* Accepts user questions
* Retrieves relevant transcript chunks
* Generates answers using retrieved context
* Supports conversational question answering

---

### Task 10 – Testing & Evaluation

Tested chatbot with multiple questions related to the video.

Verified:

* Answers originated from transcript content
* Retrieval quality was satisfactory
* Unknown questions were handled gracefully

---

## Key Concepts Learned

### Retrieval-Augmented Generation (RAG)

RAG combines:

```text
User Query
      ↓
Retriever
      ↓
Relevant Documents
      ↓
LLM
      ↓
Grounded Response
```

This approach reduces hallucinations and improves factual accuracy.

---

## Retriever Types

### Similarity Search

Returns documents most similar to the query.

### MMR (Maximal Marginal Relevance)

Returns relevant and diverse documents.

### Multi-Query Retrieval

Generates multiple query formulations to improve retrieval.

### Contextual Compression

Filters retrieved documents to retain only useful information.

---

## Vector Stores

### ChromaDB

Advantages:

* Persistent storage
* Easy LangChain integration
* Suitable for small and medium projects

### FAISS

Advantages:

* Extremely fast retrieval
* Efficient similarity search
* Suitable for large-scale systems

---

## Observations

### Retriever-Based RAG vs Normal Prompting

Normal prompting relies only on model knowledge.

RAG retrieves external information and provides grounded answers.

---

### Why Vector Stores Are Important

Vector stores:

* Store embeddings efficiently
* Enable semantic search
* Support scalable retrieval systems

---

### MMR vs Similarity Search

Similarity Search:

* Highest relevance

MMR:

* Relevance + diversity
* Avoids duplicate information

---

### Benefits of Multi-Query Retrieval

* Better recall
* Improved document coverage
* Handles ambiguous queries

---

### Importance of Contextual Compression

* Reduces noise
* Saves tokens
* Improves response quality

---

## Future Enhancements

* Streamlit Chat Interface
* Conversation Memory
* Hybrid Search
* Multi-Document RAG
* PDF + Website + YouTube Unified Assistant
* Local LLM Integration with Ollama

---

## Conclusion

This assignment provided hands-on experience with modern Retrieval-Augmented Generation pipelines, retrievers, vector databases, and document-grounded question answering systems. These components form the foundation of production-grade AI assistants and enterprise RAG applications.
