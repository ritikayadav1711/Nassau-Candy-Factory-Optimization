import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Nassau Candy Optimization",
    layout="wide"
)

st.title("Factory Reallocation & Shipping Optimization")

# Load Dataset
df = pd.read_excel("Nassau Candy Distributor.xlsx")

# KPIs
st.subheader("Project Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Orders",
    len(df)
)

col2.metric(
    "Total Sales",
    round(df["Sales"].sum(),2)
)

col3.metric(
    "Total Profit",
    round(df["Gross Profit"].sum(),2)
)

st.divider()

# Region Analysis
st.subheader("Sales by Region")

sales_region = df.groupby(
    "Region"
)["Sales"].sum()

st.bar_chart(sales_region)

# Ship Mode Analysis
st.subheader("Sales by Ship Mode")

sales_ship = df.groupby(
    "Ship Mode"
)["Sales"].sum()

st.bar_chart(sales_ship)

# Product Selector
st.subheader("Product Analysis")

product = st.selectbox(
    "Select Product",
    sorted(df["Product Name"].unique())
)

filtered = df[
    df["Product Name"] == product
]

st.write(filtered.head())

# Recommendation Table
st.subheader("Factory Recommendations")

recommendations = df.groupby(
    ["Product Name"]
)["Gross Profit"].sum().reset_index()

recommendations = recommendations.sort_values(
    "Gross Profit",
    ascending=False
)

st.dataframe(
    recommendations.head(10)
)

st.success(
    "Optimization Dashboard Loaded Successfully"
)
