import os

from langchain_ollama import OllamaLLM

# LangSmith Tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "Assignment24"

# Ollama Model
llm = OllamaLLM(
    model="llama3"
)

# User Prompt
response = llm.invoke(
    "What is Retrieval Augmented Generation?"
)

print("\nResponse:")
print(response)