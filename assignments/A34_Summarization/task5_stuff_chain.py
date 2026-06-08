from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/sample_document.txt")
docs = loader.load()

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

chain = load_summarize_chain(
    llm,
    chain_type="stuff"
)

summary = chain.invoke(docs)

print(summary["output_text"])