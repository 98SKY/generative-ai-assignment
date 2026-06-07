import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def groq_chat(prompt: str):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content