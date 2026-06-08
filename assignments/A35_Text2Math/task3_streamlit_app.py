import streamlit as st

from langchain_groq import ChatGroq
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.tools import Tool

# ---------------------------
# LLM
# ---------------------------

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# ---------------------------
# Tool
# ---------------------------

def calculator(expression: str):
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)

tool = Tool(
    name="Calculator",
    func=calculator,
    description="Useful for solving mathematical expressions."
)

agent = initialize_agent(
    tools=[tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)

# ---------------------------
# Session State
# ---------------------------

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Text-to-Math Agent")

question = st.text_input("Enter Math Question")

if st.button("Solve"):

    result = agent.invoke(question)

    answer = result["output"]

    st.session_state.history.append(
        {
            "question": question,
            "answer": answer
        }
    )

# ---------------------------
# Display History
# ---------------------------

st.subheader("Conversation History")

for item in st.session_state.history:

    st.write("Question:", item["question"])
    st.write("Answer:", item["answer"])
    st.write("---")