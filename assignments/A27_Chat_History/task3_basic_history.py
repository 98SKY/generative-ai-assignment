from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

history = []

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    history.append(
        {
            "role": "user",
            "content": question
        }
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=history
    )

    answer = response.choices[0].message.content

    history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    print("\nBot:", answer)