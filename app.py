import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Money Dashboard", page_icon="💰", layout="wide")
st.title("💰 Money Dashboard")

st.subheader("Upload Transactions")
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx", "xls"])

if uploaded_file is None:
    st.info("Upload a file with columns: date, category, description, amount, type (income/expense).")
    st.stop()

# ---- Load ----
try:
    if uploaded_file.name.lower().endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
except Exception as e:
    st.error(f"Couldn't read the file: {e}")
    st.stop()

# ---- Clean ----
df.columns = df.columns.str.strip().str.lower()
required = {"date", "category", "description", "amount", "type"}
missing = required - set(df.columns)
if missing:
    st.error(f"Missing column(s): {', '.join(sorted(missing))}")
    st.stop()

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
df["type"] = df["type"].astype(str).str.strip().str.lower()
df = df.dropna(subset=["date", "amount"])
df = df[df["type"].isin(["income", "expense"])]

if df.empty:
    st.warning("No valid rows found in this file.")
    st.stop()

st.success(f"Analyzing **{uploaded_file.name}**: {len(df)} valid rows")

income = df.loc[df["type"] == "income", "amount"].sum()
expense = df.loc[df["type"] == "expense", "amount"].sum()

# ---- KPIs ----
st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("Total Income", f"₹{income:,.2f}")
c2.metric("Total Expense", f"₹{expense:,.2f}")
c3.metric("Net Balance", f"₹{income - expense:,.2f}")
st.divider()

# ---- Category breakdown ----
exp = df[df["type"] == "expense"]
cat = exp.groupby("category", as_index=False)["amount"].sum().rename(columns={"amount": "total"})
cat = cat.sort_values("total", ascending=False)
cat["pct_of_total"] = (cat["total"] / cat["total"].sum() * 100).round(2)

left, right = st.columns(2)
with left:
    st.subheader("Spend by Category")
    if cat.empty:
        st.write("No expenses in this file.")
    else:
        st.plotly_chart(px.pie(cat, names="category", values="total"), use_container_width=True)
with right:
    st.subheader("Category % of Total Spend")
    st.dataframe(cat.reset_index(drop=True), width="stretch")

# ---- Monthly income vs expense ----
df["month"] = df["date"].dt.to_period("M").astype(str)
monthly = df.groupby(["month", "type"], as_index=False)["amount"].sum()
st.subheader("Monthly Income vs Expense")
st.plotly_chart(px.bar(monthly, x="month", y="amount", color="type", barmode="group"),
                use_container_width=True)

# ---- Running balance ----
st.subheader("Running Balance")
tmp = df.sort_values("date").copy()
tmp["signed"] = tmp["amount"].where(tmp["type"] == "income", -tmp["amount"])
tmp["balance"] = tmp["signed"].cumsum()
st.plotly_chart(px.line(tmp, x="date", y="balance", markers=True), use_container_width=True)

# ---- Top 5 expenses ----
st.subheader("Top 5 Expenses")
top5 = exp.nlargest(5, "amount")[["date", "category", "description", "amount"]]
st.dataframe(top5, width="stretch")