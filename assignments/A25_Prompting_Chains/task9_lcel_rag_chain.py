from langchain_core.prompts import PromptTemplate
from langchain_community.llms.fake import FakeListLLM

llm = FakeListLLM(
    responses=[
        "RAG combines retrieval and generation."
    ]
)

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Context:
{context}

Question:
{question}

Answer:
"""
)

rag_chain = prompt | llm

result = rag_chain.invoke(
    {
        "context":
        "RAG retrieves documents before generation.",

        "question":
        "What is RAG?"
    }
)

print(result)