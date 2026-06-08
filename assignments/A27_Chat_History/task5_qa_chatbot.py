from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

messages = [
    {
        "role": "system",
        "content": "You are a Python tutor."
    }
]

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    answer = response.choices[0].message.content

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    print("\nAnswer:")
    print(answer)