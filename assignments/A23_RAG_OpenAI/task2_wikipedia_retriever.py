from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    top_k_results=3
)

docs = retriever.invoke(
    "Artificial Intelligence"
)

print("Documents Retrieved:")
print(len(docs))

for doc in docs:
    print("\nTitle:")
    print(doc.metadata["title"])

    print("\nContent Preview:")
    print(doc.page_content[:300])