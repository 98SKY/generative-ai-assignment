from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("data/sample_document.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

chain = load_summarize_chain(
    llm,
    chain_type="map_reduce"
)

summary = chain.invoke(chunks)

print(summary["output_text"])