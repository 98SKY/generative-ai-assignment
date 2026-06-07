# Assignment 25: Prompting & LangChain Chains

## Objective

This assignment focuses on understanding Prompt Engineering, Structured Outputs, LangChain Chains, Runnables, and LCEL (LangChain Expression Language).

The goal is to learn how modern Generative AI applications are built using modular and reusable LangChain components.

---

## Technologies Used

* Python
* LangChain
* Pydantic
* FAISS (optional)
* LangChain Core
* LangChain Community

---

## Project Structure

```text
A25_Prompting_LangChain_Chains/
│
├── task1_prompt_template.py
├── task2_chat_prompt_template.py
├── task3_pydantic_output.py
├── task4_validation_handling.py
├── task5_simple_chain.py
├── task6_conditional_chain.py
├── task7_parallel_chain.py
├── task8_runnables.py
├── task9_lcel_rag_chain.py
├── task10_observations.md
├── requirements.txt
└── README.md
```

---

## Installation

Create and activate a virtual environment if required.

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

```txt
langchain
langchain-core
langchain-community
pydantic
faiss-cpu
```

---

# Task 1: PromptTemplate

### Objective

Create a reusable prompt template and dynamically inject user input.

### Features

* System instruction
* User question placeholder
* Dynamic prompt generation

---

# Task 2: ChatPromptTemplate

### Objective

Create structured chat messages using:

* System Message
* Human Message
* AI Message (optional)

### Benefits

Chat prompts provide better conversation structure than plain text prompts.

---

# Task 3: Pydantic Output Schema

### Objective

Generate structured outputs using Pydantic models.

### Schema

```python
class Answer(BaseModel):
    answer: str
    confidence: float
    source: str
```

### Benefits

* Predictable responses
* Easy validation
* Machine-readable outputs

---

# Task 4: Validation & Error Handling

### Objective

Validate generated outputs and handle malformed responses.

### Features

* Pydantic ValidationError handling
* Fallback mechanism
* Reliable application behavior

---

# Task 5: Simple Chain

### Objective

Build a basic LangChain pipeline:

```text
Prompt → LLM → Output
```

### Benefits

* Reusable workflow
* Modular architecture

---

# Task 6: Conditional Chain

### Objective

Route questions based on their type.

### Logic

Factual Questions:

```text
Question → Retriever → Answer
```

Creative Questions:

```text
Question → LLM → Answer
```

### Example

Input:

```text
What is RAG?
```

Output:

```text
Using Retriever
```

Input:

```text
Write a poem on AI
```

Output:

```text
Using Direct LLM
```

---

# Task 7: Parallel Chain

### Objective

Execute multiple tasks simultaneously.

### Parallel Tasks

* Generate Answer
* Generate Summary
* Generate Follow-up Questions

### Benefits

* Faster execution
* Better user experience

---

# Task 8: Runnables & LCEL

### Objective

Convert traditional chains into reusable runnables.

### Components

* RunnablePassthrough
* RunnableLambda
* LCEL operators (`|`)

### Benefits

* Cleaner syntax
* Easy composition
* Better maintainability

---

# Task 9: LCEL-Based RAG Chain

### Objective

Build a Retrieval-Augmented Generation workflow using LCEL.

### Pipeline

```text
Retriever
     │
     ▼
Prompt Template
     │
     ▼
LLM
     │
     ▼
Output Parser
```

### Benefits

* Modular design
* Easy debugging
* Production-ready architecture

---

# Task 10: Observations

## 1. Why structured output is important

Structured outputs make AI responses predictable, validated, and easier to integrate with applications.

## 2. Advantages of LCEL over traditional chains

* Simpler syntax
* Better readability
* Supports composition
* Supports parallel execution
* Easier maintenance

## 3. When to use parallel vs conditional chains

### Parallel Chains

Use when multiple independent tasks can run simultaneously.

Examples:

* Answer generation
* Summarization
* Follow-up question generation

### Conditional Chains

Use when workflow depends on input type.

Examples:

* Factual questions
* Creative writing
* Classification workflows

---

# Expected Outputs

Capture screenshots of:

1. PromptTemplate output
2. ChatPromptTemplate output
3. Pydantic structured output
4. Validation error handling
5. Simple chain result
6. Conditional chain result
7. Parallel chain result
8. Runnable output
9. LCEL chain output
10. Project folder structure

---

# Learning Outcomes

After completing this assignment, you will understand:

* Prompt Engineering
* Chat Prompt Templates
* Structured Outputs
* Pydantic Validation
* LangChain Chains
* Conditional Workflows
* Parallel Processing
* Runnables
* LCEL
* Foundations of RAG Pipelines

---

## Author

Sunil Kumar

Full Stack Developer | Generative AI Learner
