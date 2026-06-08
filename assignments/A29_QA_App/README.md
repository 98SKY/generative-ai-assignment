# Assignment 29: Q&A Chatbot Application (OpenAI & Ollama)

## Objective

Build two Question & Answer chatbot applications:

1. OpenAI-based chatbot (cloud LLM)
2. Ollama-based chatbot (local open-source LLM)

The assignment demonstrates the differences between cloud-hosted and locally hosted Large Language Models and provides a unified chatbot interface that can switch between models.

---

## Project Structure

```text
A29_QA_Chatbot/

├── requirements.txt

├── task1_openai_setup.py

├── task2_openai_chatbot.py

├── task3_multiturn_chat.py

├── task4_ollama_setup.md

├── task5_ollama_chatbot.py

├── task6_comparison.md

├── task7_model_switch.py

├── task8_chatbot_app.py

└── task9_observations.md
```

---

## Prerequisites

* Python 3.10+
* LangChain
* OpenAI API Key
* Ollama Installed (Optional)
* Internet Connection (for OpenAI)

---

## Installation

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

### OpenAI

```bash
export OPENAI_API_KEY="your_api_key"
```

### Groq (Optional Alternative)

```bash
export GROQ_API_KEY="your_api_key"
```

Verify:

```bash
echo $OPENAI_API_KEY
```

or

```bash
echo $GROQ_API_KEY
```

---

# PART 1 - OpenAI Chatbot

## Task 1: OpenAI Setup

Initialize OpenAI chat model using LangChain.

Run:

```bash
python task1_openai_setup.py
```

Expected Output:

```text
Generative AI refers to...
```

---

## Task 2: Basic OpenAI Q&A Chatbot

Features:

* System Prompt
* User Question
* Chat Response

Run:

```bash
python task2_openai_chatbot.py
```

Test Questions:

* What is AI?
* What is Python?
* What is LangChain?
* What is RAG?
* What is Machine Learning?

---

## Task 3: Multi-Turn Chat

Features:

* Conversation History
* Follow-up Questions

Run:

```bash
python task3_multiturn_chat.py
```

Example:

```text
User: What is Python?

Bot: Python is a programming language.

User: Give an example.
```

---

# PART 2 - Ollama Chatbot

## Task 4: Ollama Setup

Install Ollama:

```bash
brew install ollama
```

Pull Model:

```bash
ollama pull llama3
```

Verify:

```bash
ollama list
```

Start Service:

```bash
ollama serve
```

---

## Task 5: Ollama Chat Model

Run:

```bash
python task5_ollama_chatbot.py
```

Expected Output:

```text
Generative AI is a type of artificial intelligence...
```

---

## Task 6: OpenAI vs Ollama Comparison

Comparison Areas:

* Response Quality
* Latency
* Cost
* Privacy

See:

```text
task6_comparison.md
```

---

# PART 3 - Unified Chatbot

## Task 7: Model Switch Logic

Allows switching between:

* OpenAI
* Ollama

Run:

```bash
python task7_model_switch.py
```

---

## Task 8: Chatbot Application

CLI-based chatbot application.

Run:

```bash
python task8_chatbot_app.py
```

Example:

```text
Choose model: openai

You: What is RAG?

Bot: Retrieval-Augmented Generation...
```

Exit:

```text
exit
```

---

# PART 4 - Observations

## Task 9

See:

```text
task9_observations.md
```

Topics Covered:

1. When to prefer OpenAI models
2. When to prefer open-source models
3. Production trade-offs
4. Cost and scalability considerations

---

# Key Learnings

* Building conversational Q&A chatbots
* Prompt engineering using LangChain
* OpenAI integration
* Ollama integration
* Multi-turn conversations
* Model abstraction and switching
* Comparing cloud vs local LLM deployments

---

# Conclusion

This assignment demonstrates how to build conversational AI applications using both cloud-based and local LLMs. It highlights the practical differences between OpenAI and Ollama while implementing a reusable chatbot architecture suitable for real-world applications.
