import streamlit as st

def select_time_period_and_metric():
    st.sidebar.title("Select a time period")
    time_period = st.sidebar.selectbox("Select Time Period:", ["YTD", "MTD", "Last Year"], index=0)

    st.sidebar.title("Select a metric to view")
    metric = st.sidebar.selectbox(
        "Select Metric:",
        ["Total Revenue", "Headcount", "Revenue per Employee"],  # You can expand this list
        index=0
    )

    return time_period, metric
