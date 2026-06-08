from langchain_core.messages import (
    HumanMessage
)

history = []

for i in range(20):

    history.append(
        HumanMessage(
            content=f"Message {i}"
        )
    )

MAX_MESSAGES = 10

history = history[-MAX_MESSAGES:]

print(
    "Messages Left:",
    len(history)
)