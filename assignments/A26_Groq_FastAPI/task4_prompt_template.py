import os
from groq import Groq

from langchain_core.prompts import PromptTemplate

# -----------------------------
# GROQ CLIENT
# -----------------------------

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# -----------------------------
# PROMPT TEMPLATE
# -----------------------------

rag_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful AI assistant.

Use ONLY the provided context.

If the answer is not available in the context,
reply:

"I could not find that information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""
)

# -----------------------------
# SAMPLE DATA
# -----------------------------

context = """
Retrieval Augmented Generation (RAG) is a technique that combines
document retrieval with large language models.
It improves answer accuracy by grounding responses in external data.
"""

question = "What is RAG?"

# -----------------------------
# CREATE PROMPT
# -----------------------------

final_prompt = rag_prompt.format(
    context=context,
    question=question
)

print("\nGenerated Prompt:\n")
print(final_prompt)

# -----------------------------
# SEND TO GROQ
# -----------------------------

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": final_prompt
        }
    ]
)

print("\nAnswer:\n")
print(response.choices[0].message.content)