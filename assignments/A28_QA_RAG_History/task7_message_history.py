from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

history = []

history.append(
    HumanMessage(
        content="What is Python?"
    )
)

history.append(
    AIMessage(
        content="Python is a programming language."
    )
)

history.append(
    HumanMessage(
        content="Give an example."
    )
)

for msg in history:
    print(msg)