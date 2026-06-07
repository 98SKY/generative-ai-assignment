"""
Could not execute because:

macOS version: 12.7.6
Ollama requires macOS 14+

Code below works on supported systems.
"""

from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector = embeddings.embed_query(
    "LangChain helps build AI apps"
)

print(len(vector))