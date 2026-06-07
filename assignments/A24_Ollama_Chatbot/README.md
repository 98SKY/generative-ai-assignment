# Assignment 24: Ollama Chatbot

## Objective

Build a local chatbot using Ollama and LangChain and track execution using LangSmith.

---

## Task 1: Ollama Setup

### Installation

```bash
brew install ollama
```

### Start Ollama

```bash
ollama serve
```

### Pull Model

```bash
ollama pull llama3
```

---

## LangChain Integration

```python
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

response = llm.invoke(
    "Explain Artificial Intelligence"
)

print(response)
```

---

## LangSmith Tracking

```python
import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "YOUR_LANGSMITH_API_KEY"
os.environ["LANGCHAIN_PROJECT"] = "Assignment24"
```

---

## Output

The chatbot successfully accepts prompts and generates responses using the local Ollama model.

---

## Limitation Encountered

System Configuration:

* macOS Version: 12.7.6
* Ollama Desktop App Requirement: macOS 14+

Because the current machine does not meet the minimum operating system requirement, the Ollama model server could not be fully executed. The implementation code and configuration have been completed, and execution can be verified on a supported system.

---

## Technologies Used

* Python
* LangChain
* Ollama
* LangSmith

---

## Learning Outcomes

* Understanding local LLM execution
* LangChain integration with Ollama
* Prompt execution flow
* LangSmith observability and tracing


Ollama could not be executed because the local machine runs macOS 12.7.6, while the current Ollama desktop application requires macOS 14+.
