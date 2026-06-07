import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer clearly and concisely.
"""


def groq_chat(prompt: str):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message.content


# Test Queries

queries = [
    "What is Generative AI?",
    "Explain RAG in simple words.",
    "What is FastAPI?"
]

for q in queries:
    print("\nQuestion:", q)
    print("Answer:", groq_chat(q))
    print("-" * 50)