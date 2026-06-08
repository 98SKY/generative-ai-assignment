from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

loader = TextLoader("data/sample_document.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)


def summarize_document(method="map_reduce"):

    chain = load_summarize_chain(
        llm,
        chain_type=method
    )

    result = chain.invoke(chunks)

    return result["output_text"]


print(summarize_document("stuff"))

print("\n======================\n")

print(summarize_document("map_reduce"))

print("\n======================\n")

print(summarize_document("refine"))