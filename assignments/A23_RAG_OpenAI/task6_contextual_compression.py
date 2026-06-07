from langchain_openai import ChatOpenAI
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

compressor = LLMChainExtractor.from_llm(
    llm
)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever
)

docs = compression_retriever.invoke(
    "Artificial Intelligence"
)

for doc in docs:
    print(doc.page_content)