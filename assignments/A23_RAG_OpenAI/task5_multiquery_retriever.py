from langchain_openai import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

multi_query = MultiQueryRetriever.from_llm(
    retriever=retriever,
    llm=llm
)

docs = multi_query.invoke(
    "Explain artificial intelligence"
)

for doc in docs:
    print(doc.page_content)