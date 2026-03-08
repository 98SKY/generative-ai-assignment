import streamlit as st

# Title of the app
st.title("Welcome to Streamlit!")

# Text input for user name
name = st.text_input("Enter your name:")

# Button to greet user
if st.button("Greet Me"):
    if name:
        st.write(f"Hello, {name}!")
    else:
        st.write("Please enter your name.")