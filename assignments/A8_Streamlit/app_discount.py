import streamlit as st

st.title("Price Calculator")

# Input product price
price = st.number_input("Enter product price:", min_value=0.0)

# Discount slider
discount = st.slider("Select discount percentage:", 0, 50)

# Button to calculate final price
if st.button("Calculate Final Price"):

    final_price = price - (price * discount / 100)

    st.success(f"Final Price: ₹{final_price:.2f}")

    # Optional comparison table
    st.write("### Price Comparison")

    data = [
        ["Original Price", price],
        ["Discount (%)", discount],
        ["Final Price", final_price]
    ]

    st.table(data)