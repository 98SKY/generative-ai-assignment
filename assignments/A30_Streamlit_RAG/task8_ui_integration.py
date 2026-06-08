import streamlit as st

st.title(
    "ChatGroq RAG"
)

if "messages" not in st.session_state:

    st.session_state.messages = []

question = st.chat_input(
    "Ask a question..."
)

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    answer = f"Answer for: {question}"

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

for msg in st.session_state.messages:

    st.chat_message(
        msg["role"]
    ).write(
        msg["content"]
    )