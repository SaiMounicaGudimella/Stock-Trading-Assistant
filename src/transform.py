import pandas as pd
import numpy as np

def transform_data(df):
    df = df.sort_values(["ticker", "Date"])
    
    # --- Moving Averages ---
    df["MA50"] = df.groupby("ticker")["Close"].transform(lambda x: x.rolling(50, min_periods=1).mean())
    df["MA200"] = df.groupby("ticker")["Close"].transform(lambda x: x.rolling(200, min_periods=1).mean())
    
    # --- Generate BUY Signal ---
    df["Signal"] = np.where(df["MA50"] > df["MA200"], "BUY", "HOLD")

    # --- Daily Returns ---
    df["Return"] = df.groupby("ticker")["Close"].pct_change().fillna(0)

    # --- Strategy Returns (buy when MA50 > MA200) ---
    df["Strategy_Return"] = np.where(df["Signal"].shift(1) == "BUY", df["Return"], 0)

    # --- Cumulative Returns ---
    df["Cumulative_Market"] = df.groupby("ticker")["Return"].apply(lambda x: (1 + x).cumprod())
    df["Cumulative_Strategy"] = df.groupby("ticker")["Strategy_Return"].apply(lambda x: (1 + x).cumprod())

    # --- Buy Markers for Plotting ---
    df["Buy_Marker"] = np.where((df["Signal"] == "BUY") & (df["Signal"].shift(1) == "HOLD"), df["Close"], np.nan)

    return df
