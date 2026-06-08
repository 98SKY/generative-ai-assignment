import os
import tempfile

import streamlit as st

from langchain_groq import ChatGroq

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import (
    FAISS
)

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="ChatGroq RAG Chatbot",
    page_icon="🤖"
)

st.title("🤖 ChatGroq RAG Chatbot")

# ------------------------------------
# SESSION STATE
# ------------------------------------

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "history" not in st.session_state:
    st.session_state.history = []

# ------------------------------------
# FILE UPLOAD
# ------------------------------------

uploaded_file = st.file_uploader(
    "Upload PDF or TXT File",
    type=["pdf", "txt"]
)

# ------------------------------------
# PROCESS DOCUMENT
# ------------------------------------

if uploaded_file and st.session_state.vectorstore is None:

    with st.spinner("Processing document..."):

        suffix = (
            ".pdf"
            if uploaded_file.name.endswith(".pdf")
            else ".txt"
        )

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as tmp:

            tmp.write(
                uploaded_file.read()
            )

            file_path = tmp.name

        if suffix == ".pdf":

            loader = PyPDFLoader(
                file_path
            )

        else:

            loader = TextLoader(
                file_path
            )

        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(
            docs
        )

        embeddings = HuggingFaceEmbeddings(
            model_name=
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        vectorstore = FAISS.from_documents(
            chunks,
            embeddings
        )

        st.session_state.vectorstore = vectorstore

    st.success(
        f"Document processed. Chunks: {len(chunks)}"
    )

# ------------------------------------
# LLM
# ------------------------------------

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

# ------------------------------------
# PROMPT
# ------------------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a helpful AI assistant.

Answer ONLY from the provided context.

If answer is not available,
reply:

I don't know.
"""
        ),

        MessagesPlaceholder(
            variable_name="history"
        ),

        (
            "human",
            """
Context:
{context}

Question:
{question}
"""
        )
    ]
)

# ------------------------------------
# DISPLAY CHAT HISTORY
# ------------------------------------

for msg in st.session_state.history:

    if isinstance(
        msg,
        HumanMessage
    ):

        st.chat_message(
            "user"
        ).write(
            msg.content
        )

    else:

        st.chat_message(
            "assistant"
        ).write(
            msg.content
        )

# ------------------------------------
# CHAT INPUT
# ------------------------------------

question = st.chat_input(
    "Ask a question..."
)

if (
    question
    and
    st.session_state.vectorstore
):

    st.chat_message(
        "user"
    ).write(
        question
    )

    retriever = (
        st.session_state
        .vectorstore
        .as_retriever(
            search_kwargs={
                "k": 3
            }
        )
    )

    docs = retriever.invoke(
        question
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question,
            "history":
            st.session_state.history
        }
    )

    answer = response.content

    st.chat_message(
        "assistant"
    ).write(
        answer
    )

    st.session_state.history.append(
        HumanMessage(
            content=question
        )
    )

    st.session_state.history.append(
        AIMessage(
            content=answer
        )
    )

    # Keep only last 10 messages

    if (
        len(
            st.session_state.history
        ) > 10
    ):
        st.session_state.history = (
            st.session_state.history[-10:]
        )