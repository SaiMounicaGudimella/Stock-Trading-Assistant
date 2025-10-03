import yfinance as yf
import duckdb
import pandas as pd
from datetime import datetime

# 1. Download stock data
ticker = "AAPL"
df = yf.download(ticker, period="3y", interval="1d")
df.reset_index(inplace=True)

df.head()

df.columns = df.columns.droplevel(1)
df['Ticker'] = ticker

df.head()

# 2. Store in DuckDB (lightweight SQL database file)
conn = duckdb.connect("stocks.duckdb")
conn.execute("DROP TABLE IF EXISTS stock_data") # Drop the table if it exists
conn.execute("CREATE TABLE stock_data AS SELECT * FROM df") # Recreate the table with the updated DataFrame
conn.execute("INSERT INTO stock_data SELECT * FROM df")

# 3. Query back
result = conn.execute("SELECT Date, Close FROM stock_data LIMIT 5").fetchdf()
result = conn.execute("SELECT * FROM stock_data LIMIT 5").fetchdf()
print(result)

# 4. Add a quick signal
df["MA50"] = df["Close"].rolling(50).mean()
df["MA200"] = df["Close"].rolling(200).mean()
latest = df.iloc[-1]
if latest["MA50"] > latest["MA200"]:
    print("📈 BUY signal for", ticker)
else:
    print("📉 No Buy signal yet")

df.head(-5)

# 5. Save as CSV (to commit into GitHub) 
os.makedirs("data", exist_ok=True)
csv_path = f"data/{ticker}_history.csv"
df.to_csv(csv_path, index=False)

print(f"✅ Data saved to {csv_path}")
