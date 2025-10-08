import pandas as pd
import numpy as np

def backtest_strategy(df):
    results = []

    for ticker, tdf in df.groupby("ticker"):
        tdf = tdf.dropna(subset=["MA50", "MA200"])
        tdf = tdf.sort_values("Date")

        # Generate signals
        tdf["Signal"] = np.where(tdf["MA50"] > tdf["MA200"], 1, 0)  # 1 = buy, 0 = hold

        # Daily returns
        tdf["Return"] = tdf["Close"].pct_change()

        # Strategy returns (holding when Signal == 1)
        tdf["Strategy"] = tdf["Signal"].shift(1) * tdf["Return"]

        # Performance metrics
        total_return = (1 + tdf["Strategy"]).prod() - 1
        sharpe = np.sqrt(252) * tdf["Strategy"].mean() / tdf["Strategy"].std() if tdf["Strategy"].std() != 0 else 0

        results.append({
            "Ticker": ticker,
            "Total Return (%)": round(total_return * 100, 2),
            "Sharpe Ratio": round(sharpe, 2),
        })

    return pd.DataFrame(results)
