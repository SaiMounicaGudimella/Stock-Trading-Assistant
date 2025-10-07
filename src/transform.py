import pandas as pd

def transform_data(df):
    df["MA50"] = df.groupby("ticker")["Close"].transform(lambda x: x.rolling(50).mean())
    df["MA200"] = df.groupby("ticker")["Close"].transform(lambda x: x.rolling(200).mean())
    df["Signal"] = df.apply(
        lambda x: "BUY" if x["MA50"] > x["MA200"] else "HOLD", axis=1
    )
    return df
