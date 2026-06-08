from transformers import pipeline

from langchain_huggingface import HuggingFacePipeline

from langchain_core.prompts import ChatPromptTemplate

pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=150
)

llm = HuggingFacePipeline(
    pipeline=pipe
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant."
        ),
        (
            "human",
            "{question}"
        )
    ]
)

chain = prompt | llm

response = chain.invoke(
    {
        "question":
        "Explain vector databases."
    }
)

print("\nResponse:")
print(response)