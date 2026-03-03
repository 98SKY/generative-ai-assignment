import streamlit as st

st.title("Welcome to Streamlit!")

name = st.text_input("Enter your name:")

if st.button("Greet Me"):
    if name:
        st.write(f"Hello, {name}!")
    else:
        st.write("Please enter your name.")