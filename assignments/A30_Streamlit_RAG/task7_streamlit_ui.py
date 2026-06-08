import streamlit as st

st.title(
    "ChatGroq RAG Chatbot"
)

question = st.chat_input(
    "Ask a question..."
)

if question:

    st.chat_message(
        "user"
    ).write(question)

    st.chat_message(
        "assistant"
    ).write("Sample Response")