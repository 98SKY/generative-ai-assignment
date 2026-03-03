import streamlit as st

st.header("Welcome to Streamlint Project")
st.title("Our first project!!")
st.subheader("Lets build some ui")

st.text("hey there")

if st.button("Click Me"):
    st.text("Button Clicked !!")

agree = st.checkbox("I am agree")
if agree:
    st.write("You are agree !!")

level = st.slider("Select a level:", 0,5,10)
st.write(f"selected level is: {level}")

upload_file = st.file_uploader("Select file", type=["png, jpeg, jpg"])