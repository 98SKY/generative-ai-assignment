import streamlit as st

st.title("Simple Sales Dashboard")
st.write("Select a month to view sales data.")

months = ["January", "February", "March", "April"]

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

selected_month = st.selectbox("Choose Month:", months)

# Show selected month sales
st.metric("Sales for Selected Month", sales[selected_month])

# Bar chart of all months
st.write("### Monthly Sales Overview")

st.bar_chart(list(sales.values()))