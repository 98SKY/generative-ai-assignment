from langchain_core.prompts import (
    ChatPromptTemplate
)

prompt = ChatPromptTemplate.from_template(
"""
Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

If answer is not found,
say:
I don't know.
"""
)

print(prompt)