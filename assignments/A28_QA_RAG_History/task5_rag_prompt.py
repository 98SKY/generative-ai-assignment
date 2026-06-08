from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Answer only from retrieved context.
            If answer is not available say:
            I don't know.
            """
        ),

        MessagesPlaceholder(
            variable_name="history"
        ),

        (
            "human",
            """
            Context:
            {context}

            Question:
            {question}
            """
        )
    ]
)

print(prompt)