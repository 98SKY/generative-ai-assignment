import streamlit as st

from codellama_assistant import (
    generate_code,
    explain_code,
    debug_code,
    optimize_code
)

st.set_page_config(
    page_title="AI Coding Assistant",
    layout="wide"
)

st.title("CodeLlama Coding Assistant")

task = st.selectbox(
    "Select Task",
    [
        "Generate Code",
        "Explain Code",
        "Debug Code",
        "Optimize Code"
    ]
)

user_input = st.text_area(
    "Enter prompt or code",
    height=300
)

if st.button("Submit"):

    if task == "Generate Code":
        result = generate_code(user_input)

    elif task == "Explain Code":
        result = explain_code(user_input)

    elif task == "Debug Code":
        result = debug_code(user_input)

    else:
        result = optimize_code(user_input)

    st.subheader("Result")

    st.code(result)