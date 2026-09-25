import streamlit as st
import database

st.title("Personal Expense Dashboard")

try:
    expenses = database.get_expenses()
except Exception as exc:
    st.error(f"Could not load expenses from MySQL: {exc}")
    st.stop()

if expenses.empty:
    st.info("No expenses found. Run main.py to load your data first." )
else:
    st.metric("Total expenses", f"${expenses['Amount'].sum():,.2f}")
    st.subheader("Spending by category")
    st.bar_chart(expenses.groupby("Category")["Amount"].sum())
    st.subheader("Transactions")
    st.dataframe(expenses, width="stretch")