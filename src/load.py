import duckdb

def load_data(df, db_path="data/stocks.duckdb"):
    conn = duckdb.connect(db_path)
    conn.execute("CREATE TABLE IF NOT EXISTS stock_data AS SELECT * FROM df LIMIT 0")
    conn.execute("INSERT INTO stock_data SELECT * FROM df")
    conn.close()
