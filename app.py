import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

st.title("📈 Stock Dashboard")

ticker = st.text_input("Enter ticker", "AAPL")

df = yf.download(ticker, period="6mo", interval="1d")
df.columns = df.columns.droplevel(1)
#df['Ticker'] = ticker

# Calculate signals
df["MA50"] = df["Close"].rolling(50).mean()
df["MA200"] = df["Close"].rolling(200).mean()

st.line_chart(df[["Close", "MA50", "MA200"]])

latest = df.iloc[-1]
if latest["MA50"] > latest["MA200"]:
    st.success(f"📈 BUY signal for {ticker}")
else:
    st.error(f"📉 No Buy signal yet")


def plot_backtest(df, ticker="AAPL"):
    tdf = df[df["ticker"] == ticker].dropna()
    tdf["Cumulative Market"] = (1 + tdf["Return"]).cumprod()
    tdf["Cumulative Strategy"] = (1 + tdf["Strategy"]).cumprod()

    plt.figure(figsize=(10,5))
    plt.plot(tdf["Date"], tdf["Cumulative Market"], label="Market Return")
    plt.plot(tdf["Date"], tdf["Cumulative Strategy"], label="Strategy Return")
    plt.title(f"Backtest Results: {ticker}")
    plt.legend()
    plt.grid(True)
    plt.show()
