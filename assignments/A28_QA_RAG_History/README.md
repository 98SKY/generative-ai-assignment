# Assignment 28: Q&A RAG Chatbot with Message History

## Objective

Build a Conversational RAG (Retrieval-Augmented Generation) chatbot that:

* Loads documents
* Splits them into chunks
* Creates embeddings
* Stores embeddings in FAISS
* Retrieves relevant context
* Maintains conversation history
* Handles follow-up questions

---

## Technologies Used

* Python
* LangChain
* Groq API
* HuggingFace Embeddings
* FAISS

---

## Project Structure

A28_Conversational_RAG/

├── task1_load_documents.py

├── task2_text_splitter.py

├── task3_embeddings.py

├── task4_vectorstore.py

├── task5_rag_prompt.py

├── task6_rag_chain.py

├── task7_message_history.py

├── task8_trim_history.py

├── task9_testing.py

├── task10_final_chatbot.py

├── task11_observations.md

├── requirements.txt

└── README.md

---

## Installation

Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Groq API

```bash
export GROQ_API_KEY="YOUR_API_KEY"
```

Verify:

```bash
echo $GROQ_API_KEY
```

---

## Tasks

### Task 1

Load documents using:

* TextLoader
* PyPDFLoader

Run:

```bash
python task1_load_documents.py
```

---

### Task 2

Split documents using:

* RecursiveCharacterTextSplitter

Run:

```bash
python task2_text_splitter.py
```

---

### Task 3

Generate embeddings using:

* sentence-transformers/all-MiniLM-L6-v2

Run:

```bash
python task3_embeddings.py
```

---

### Task 4

Store embeddings in FAISS and create retriever.

Run:

```bash
python task4_vectorstore.py
```

---

### Task 5

Create ChatPromptTemplate with:

* System Message
* MessagesPlaceholder
* Human Message

Run:

```bash
python task5_rag_prompt.py
```

---

### Task 6

Build RAG chain:

Question → Retriever → Prompt → Groq → Answer

Run:

```bash
python task6_rag_chain.py
```

---

### Task 7

Maintain conversation history using:

* HumanMessage
* AIMessage

Run:

```bash
python task7_message_history.py
```

---

### Task 8

Trim history after max message limit.

Run:

```bash
python task8_trim_history.py
```

---

### Task 9

Test chatbot with:

1. Initial question
2. Follow-up question
3. Clarification question

Run:

```bash
python task9_testing.py
```

---

### Task 10

Final Conversational RAG Assistant.

Features:

* Retrieval
* History Management
* Context Awareness
* Follow-Up Questions

Run:

```bash
python task10_final_chatbot.py
```

Exit:

```text
exit
```

---

## Learning Outcomes

* Retrieval-Augmented Generation
* Conversational RAG
* FAISS Vector Stores
* HuggingFace Embeddings
* ChatPromptTemplate
* MessagesPlaceholder
* Stateful AI Assistants

---

## Result

Built a conversational document assistant capable of:

* Retrieving information from documents
* Remembering previous questions
* Answering follow-up queries
* Reducing hallucinations through grounding
