# Assignment 31: Conversational PDF Q&A Chatbot with Message History

## Objective

Build a conversational PDF Question Answering chatbot using:

* LangChain
* ChatGroq
* HuggingFace Embeddings
* FAISS Vector Store
* Streamlit

The chatbot should:

* Answer questions from uploaded PDF documents
* Maintain conversation history
* Support follow-up questions
* Use Retrieval Augmented Generation (RAG)
* Avoid hallucinations by grounding answers in PDF content

---

## Features

* PDF Upload
* Automatic PDF Chunking
* Embedding Generation
* FAISS Vector Database
* Conversational Retrieval
* Message History Support
* Chat History Trimming
* Streamlit User Interface

---

## Project Structure

```text
A31_Conversational_PDF_QA/

├── task1_load_pdf.py
├── task2_text_splitter.py
├── task3_embeddings.py
├── task4_vectorstore.py
├── task5_rag_prompt.py
├── task6_conversational_rag.py
├── task7_message_history.py
├── task8_trim_history.py
├── task9_testing.py
├── task10_final_chatbot.py
├── task11_observations.md
├── requirements.txt
└── data/sample.pdf
```

---

## Installation

Install dependencies:

```bash
pip install langchain
pip install langchain-community
pip install langchain-core
pip install langchain-groq
pip install langchain-huggingface
pip install langchain-text-splitters
pip install sentence-transformers
pip install faiss-cpu
pip install pypdf
pip install streamlit
```

---

## Configure Groq API Key

Linux / Mac:

```bash
export GROQ_API_KEY="your_api_key"
```

Verify:

```bash
echo $GROQ_API_KEY
```

---

## Run Application

```bash
streamlit run task10_final_chatbot.py
```

---

## Testing

Example Questions:

1. What is Retrieval Augmented Generation?
2. Explain the previous answer.
3. Give an example.
4. Summarize the previous topic.
5. What are the key points discussed?

Out-of-context Question:

```text
Who won FIFA World Cup 2022?
```

Expected:

```text
I don't know.
```

---

## Technologies Used

* LangChain
* ChatGroq
* HuggingFace Embeddings
* FAISS
* Streamlit
* Python

---

## Learning Outcomes

* PDF Loading
* Text Chunking
* Embedding Generation
* Vector Search
* Conversational RAG
* Message History Management
* Follow-up Question Handling
* Streamlit Deployment

```
```
