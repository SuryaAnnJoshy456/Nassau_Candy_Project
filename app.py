import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Nassau Candy Dashboard",
    page_icon="",
    layout="wide"
)

st.title(" Nassau Candy Distributor Dashboard")
st.markdown("### Product Line Profitability & Margin Performance Analysis")

# ----------------------------
# Load Data
# ----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/Nassau Candy Distributor.csv")
    df["Gross Margin %"] = (df["Gross Profit"] / df["Sales"]) * 100
    df["Profit Per Unit"] = df["Gross Profit"] / df["Units"]
    return df

df = load_data()

# ----------------------------
# Sidebar Filters
# ----------------------------
st.sidebar.header("Filters")

division = st.sidebar.multiselect(
    "Division",
    df["Division"].unique(),
    default=df["Division"].unique()
)

margin = st.sidebar.slider(
    "Minimum Gross Margin %",
    0,
    100,
    0
)

product = st.sidebar.text_input("Search Product")

filtered = df[
    (df["Division"].isin(division)) &
    (df["Gross Margin %"] >= margin)
]

if product:
    filtered = filtered[
        filtered["Product Name"].str.contains(product, case=False)
    ]

# ----------------------------
# KPI Cards
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${filtered['Sales'].sum():,.2f}")
col2.metric("Total Profit", f"${filtered['Gross Profit'].sum():,.2f}")
col3.metric("Average Margin", f"{filtered['Gross Margin %'].mean():.2f}%")
col4.metric("Units Sold", f"{filtered['Units'].sum():,.0f}")

st.divider()

# ----------------------------
# Revenue by Division
# ----------------------------
division_sales = filtered.groupby("Division")["Sales"].sum().reset_index()

fig1 = px.bar(
    division_sales,
    x="Division",
    y="Sales",
    color="Division",
    title="Revenue by Division"
)

st.plotly_chart(fig1, use_container_width=True)

# ----------------------------
# Profit by Product
# ----------------------------
product_profit = filtered.groupby("Product Name")["Gross Profit"].sum().reset_index()

fig2 = px.bar(
    product_profit.sort_values("Gross Profit"),
    x="Gross Profit",
    y="Product Name",
    orientation="h",
    color="Gross Profit",
    title="Profit by Product"
)

st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# Cost vs Sales
# ----------------------------
fig3 = px.scatter(
    filtered,
    x="Cost",
    y="Sales",
    color="Division",
    size="Gross Profit",
    hover_name="Product Name",
    title="Cost vs Sales"
)

st.plotly_chart(fig3, use_container_width=True)

# ----------------------------
# Product Table
# ----------------------------
st.subheader("Dataset")

st.dataframe(filtered)