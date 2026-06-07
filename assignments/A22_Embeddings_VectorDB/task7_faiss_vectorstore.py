"""
FAISS installation failed on macOS due
to SWIG dependency issue.

Installation attempted:

pip install faiss-cpu

Error:
command 'swig' failed

Reference implementation:
"""

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

docs = [
    "Python programming",
    "Machine Learning",
    "Generative AI"
]

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_texts(
    docs,
    embedding_model
)

vectorstore.save_local("faiss_index")

loaded_db = FAISS.load_local(
    "faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

results = loaded_db.similarity_search(
    "Artificial Intelligence"
)

for doc in results:
    print(doc.page_content)