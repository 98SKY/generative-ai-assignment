from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

docs = [
    "Python is a programming language",
    "Machine learning uses data",
    "LangChain helps build AI applications",
    "Deep learning is a subset of ML"
]

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

doc_vectors = embedding_model.embed_documents(docs)

query = "Artificial Intelligence"

query_vector = embedding_model.embed_query(query)

scores = cosine_similarity(
    [query_vector],
    doc_vectors
)[0]

top_indices = np.argsort(scores)[::-1]

print("\nTop Similar Documents:\n")

for idx in top_indices[:3]:
    print(docs[idx])
    print("Score:", scores[idx])
    print()