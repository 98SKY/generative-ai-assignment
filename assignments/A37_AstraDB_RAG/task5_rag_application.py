import os

from dotenv import load_dotenv

from langchain_astradb import AstraDBVectorStore

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_groq import ChatGroq

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = AstraDBVectorStore(
    collection_name="assignment37",
    embedding=embeddings,
    api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"),
    token=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

while True:

    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(
        question
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer only using the provided context.

If answer is not present,
say "I don't know."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(
        prompt
    )

    print("\nAnswer:")
    print(response.content)