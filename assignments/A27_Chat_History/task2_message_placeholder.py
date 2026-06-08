import os

from groq import Groq

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

history = [
    HumanMessage(content="What is Python?"),
    AIMessage(content="Python is a programming language.")
]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder("chat_history"),
        ("human", "{question}")
    ]
)

formatted = prompt.invoke(
    {
        "chat_history": history,
        "question": "Give me an example."
    }
)

print(formatted)