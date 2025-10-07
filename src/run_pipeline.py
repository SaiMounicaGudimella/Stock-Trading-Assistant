from extract import extract_data
from transform import transform_data
from load import load_data

TICKERS = ["AAPL", "MSFT", "NVDA", "GOOG"]

if __name__ == "__main__":
    data = extract_data(TICKERS)
    transformed = transform_data(data)
    load_data(transformed)
    print("✅ ETL pipeline completed successfully!")
