import pandas as pd
import numpy as np

def calculate_performance(df):
    results = []
    for ticker, tdf in df.groupby("ticker"):
        tdf = tdf.dropna(subset=["Strategy_Return"])
        total_return = tdf["Cumulative_Strategy"].iloc[-1] - 1
        market_return = tdf["Cumulative_Market"].iloc[-1] - 1
        sharpe = (
            np.sqrt(252) * tdf["Strategy_Return"].mean() / tdf["Strategy_Return"].std()
            if tdf["Strategy_Return"].std() != 0 else 0
        )
        results.append({
            "Ticker": ticker,
            "Market Return (%)": round(market_return * 100, 2),
            "Strategy Return (%)": round(total_return * 100, 2),
            "Sharpe Ratio": round(sharpe, 2)
        })
    return pd.DataFrame(results)
