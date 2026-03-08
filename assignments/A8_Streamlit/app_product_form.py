import streamlit as st

st.title("Product Entry Form")

# Sidebar inputs
st.sidebar.header("Add Product Details")

product_name = st.sidebar.text_input("Product Name")

category = st.sidebar.selectbox(
    "Category",
    ["Electronics", "Clothing", "Books", "Home", "Sports"]
)

price = st.sidebar.number_input("Price", min_value=0.0)

# Button to add product
if st.sidebar.button("Add Product"):

    st.success("Product Added Successfully!")

    st.write("### Product Details")
    st.write(f"**Name:** {product_name}")
    st.write(f"**Category:** {category}")
    st.write(f"**Price:** ₹{price}")