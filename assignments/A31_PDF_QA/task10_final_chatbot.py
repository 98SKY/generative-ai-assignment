import os
import tempfile

import streamlit as st

from langchain_groq import ChatGroq

from langchain_community.document_loaders import (
    PyPDFLoader
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

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Conversational PDF Q&A",
    page_icon="📄"
)

st.title("📄 Conversational PDF Q&A Chatbot")

# ---------------------------------
# SESSION STATE
# ---------------------------------

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------------------------
# FILE UPLOAD
# ---------------------------------

uploaded_pdf = st.file_uploader(
    "Upload PDF Document",
    type=["pdf"]
)

# ---------------------------------
# PROCESS PDF
# ---------------------------------

if uploaded_pdf and st.session_state.vectorstore is None:

    with st.spinner("Processing PDF..."):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(uploaded_pdf.read())

            pdf_path = tmp.name

        loader = PyPDFLoader(pdf_path)

        pages = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(
            pages
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
        f"PDF Processed Successfully ({len(chunks)} Chunks)"
    )

# ---------------------------------
# GROQ MODEL
# ---------------------------------

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

# ---------------------------------
# PROMPT TEMPLATE
# ---------------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a PDF Question Answering Assistant.

Rules:
1. Answer ONLY from the PDF context.
2. Use previous conversation when needed.
3. If answer is unavailable in context,
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

# ---------------------------------
# DISPLAY CHAT HISTORY
# ---------------------------------

for msg in st.session_state.history:

    if isinstance(msg, HumanMessage):

        st.chat_message("user").write(
            msg.content
        )

    else:

        st.chat_message("assistant").write(
            msg.content
        )

# ---------------------------------
# USER QUESTION
# ---------------------------------

question = st.chat_input(
    "Ask question from PDF..."
)

if (
    question
    and
    st.session_state.vectorstore
):

    st.chat_message(
        "user"
    ).write(question)

    retriever = (
        st.session_state.vectorstore
        .as_retriever(
            search_kwargs={"k": 3}
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
    ).write(answer)

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

    # Keep last 10 messages

    MAX_MESSAGES = 10

    if len(st.session_state.history) > MAX_MESSAGES:

        st.session_state.history = (
            st.session_state.history[
                -MAX_MESSAGES:
            ]
        )