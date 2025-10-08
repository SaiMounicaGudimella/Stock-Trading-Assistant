import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="📈 Finance System Dashboard", layout="wide")

st.title("💹 Automated Financial Analytics Dashboard")

# --- Load Data ---
stocks_csv = "data/processed/stocks_latest.csv"
backtest_csv = "data/backtest_results.csv"

try:
    stocks_df = pd.read_csv(stocks_csv)
    backtest_df = pd.read_csv(backtest_csv)
except FileNotFoundError:
    st.error("Data files not found! Make sure your ETL pipeline has run at least once.")
    st.stop()

# --- Sidebar Filters ---
tickers = stocks_df["ticker"].unique().tolist()
selected_ticker = st.sidebar.selectbox("Select Stock", tickers)

# --- Display Backtest Summary ---
st.subheader("📊 Backtest Summary")
st.dataframe(backtest_df.style.highlight_max(axis=0, color='lightgreen'))

# --- Price Chart ---
st.subheader(f"📈 Price & Signals — {selected_ticker}")

tdf = stocks_df[stocks_df["ticker"] == selected_ticker].copy()
tdf["Date"] = pd.to_datetime(tdf["Date"])

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(tdf["Date"], tdf["Close"], label="Close", alpha=0.8)
ax.plot(tdf["Date"], tdf["MA50"], label="MA50", linestyle="--")
ax.plot(tdf["Date"], tdf["MA200"], label="MA200", linestyle="--")

# Highlight BUY signals
buy_points = tdf[tdf["Signal"] == "BUY"]
ax.scatter(buy_points["Date"], buy_points["Close"], color="green", label="BUY", marker="^")

ax.set_title(f"{selected_ticker} Price & Buy Signals")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# --- Footer ---
st.markdown("Last updated automatically by GitHub Actions. ✨")
