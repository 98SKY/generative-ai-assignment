from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MAX_MESSAGES = 6

history = []

def trim_history():

    global history

    if len(history) > MAX_MESSAGES:
        history = history[-MAX_MESSAGES:]

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

    trim_history()

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

    trim_history()

    print("\nBot:", answer)