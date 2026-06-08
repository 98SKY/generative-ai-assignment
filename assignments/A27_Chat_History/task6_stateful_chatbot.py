from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MAX_HISTORY = 8

history = [
    {
        "role": "system",
        "content": """
You are a helpful AI assistant.

Remember previous conversation.

Answer follow-up questions using context.
"""
    }
]

def trim_history():

    global history

    if len(history) > MAX_HISTORY:
        system = history[0]
        history = [system] + history[-(MAX_HISTORY-1):]

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    history.append(
        {
            "role": "user",
            "content": user_input
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

    print("\nBot:")
    print(answer)