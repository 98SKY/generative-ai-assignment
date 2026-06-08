from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini"
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

questions = [
    "What is AI?",
    "What is Python?",
    "What is LangChain?",
    "What is RAG?",
    "What is Machine Learning?"
]

for q in questions:

    response = chain.invoke(
        {
            "question": q
        }
    )

    print("\nQuestion:", q)
    print("Answer:", response.content)