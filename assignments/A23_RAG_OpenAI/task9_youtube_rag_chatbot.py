from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

while True:

    question = input("Ask: ")

    if question.lower() == "exit":
        break

    answer = qa_chain.invoke(
        {"query": question}
    )

    print(answer["result"])