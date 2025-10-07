import yfinance as yf
import pandas as pd
from datetime import datetime

def extract_data(tickers, period="1y", interval="1d"):
    frames = []
    for t in tickers:
        df = yf.download(t, period=period, interval=interval)
        df["ticker"] = t
        frames.append(df.reset_index())
    data = pd.concat(frames)
    data["extracted_at"] = datetime.utcnow()
    return data
