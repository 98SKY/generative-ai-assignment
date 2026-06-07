from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an AI tutor."
        ),
        (
            "human",
            "{question}"
        )
    ]
)

messages = chat_prompt.format_messages(
    question="Explain RAG."
)

for msg in messages:
    print(msg)