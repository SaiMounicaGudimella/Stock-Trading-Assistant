import duckdb
import os

def load_data(df, db_path="data/stocks.duckdb", csv_path="data/processed/stocks_latest.csv"):
    """
    Load the transformed DataFrame into both DuckDB and CSV.
    - Appends new records to DuckDB.
    - Overwrites CSV with the latest snapshot.
    """

    # Ensure directories exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    conn = duckdb.connect(db_path)
    conn.execute("CREATE TABLE IF NOT EXISTS stock_data AS SELECT * FROM df LIMIT 0")
    conn.execute("INSERT INTO stock_data SELECT * FROM df")
    conn.close()
    
    # --- Save to CSV ---
    df.to_csv(csv_path, index=False)
    print(f"✅ Data saved to DuckDB ({db_path}) and CSV ({csv_path})")
