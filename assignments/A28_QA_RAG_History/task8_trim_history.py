from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

MAX_HISTORY = 4

history = []

for i in range(10):

    history.append(
        HumanMessage(
            content=f"Question {i}"
        )
    )

    history.append(
        AIMessage(
            content=f"Answer {i}"
        )
    )

if len(history) > MAX_HISTORY:
    history = history[-MAX_HISTORY:]

print("History Length:", len(history))

for msg in history:
    print(msg.content)