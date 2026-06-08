import os

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

questions = [
    "What is AI?",
    "What is Python?",
    "What is LangChain?"
]

for q in questions:

    response = llm.invoke(q)

    print("\nQuestion:", q)
    print("Answer:", response.content)