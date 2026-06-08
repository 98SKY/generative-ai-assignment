import os

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

response = llm.invoke(
    "Explain Retrieval Augmented Generation."
)

print(
    response.content
)