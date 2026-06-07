from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["question"],
    template="""
You are an AI Assistant.

Question:
{question}

Answer:
"""
)

print(
    template.format(
        question="What is Generative AI?"
    )
)