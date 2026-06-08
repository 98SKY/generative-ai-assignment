from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Answer ONLY from PDF context.

If answer is not found,
say:

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