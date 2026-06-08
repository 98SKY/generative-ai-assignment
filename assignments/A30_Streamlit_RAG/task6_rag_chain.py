import os

from langchain_groq import ChatGroq

from langchain_core.prompts import (
    ChatPromptTemplate
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_template(
"""
Context:
{context}

Question:
{question}
"""
)

chain = prompt | llm

response = chain.invoke(
    {
        "context": "RAG means Retrieval Augmented Generation.",
        "question": "What is RAG?"
    }
)

print(response.content)