import streamlit as st
import pandas as pd

st.set_page_config(page_title="Qahwa Corner Dashboard", layout="wide")
st.title("☕ Qahwa Corner – Sales Dashboard")

df = pd.read_csv("cafe_sales.csv")
df["date"] = pd.to_datetime(df["date"])

branches = ["All"] + sorted(df["branch"].unique().tolist())
selected = st.selectbox("Select Branch", branches)

if selected != "All":
    data = df[df["branch"] == selected]
else:
    data = df

total_rev = data["total_sar"].sum()
st.metric("Total Revenue (SAR)", f"{total_rev:,.0f}")

product_rev = data.groupby("product")["total_sar"].sum().sort_values(ascending=False)
st.subheader("Revenue by Product")
st.bar_chart(product_rev)

st.caption("Data: Qahwa Corner – January to June 2026")
