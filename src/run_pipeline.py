from extract import extract_data
from transform import transform_data
from load import load_data
from backtest import backtest_strategy
from metrics import calculate_performance

TICKERS = ["AAPL"]

if __name__ == "__main__":
    print("🔹 Extracting data...")
    data = extract_data(TICKERS)

    print("🔹 Transforming data...")
    transformed = transform_data(data)

    print("🔹 Loading data...")
    load_data(transformed)

    print("🔹 Running backtest...")
    results = backtest_strategy(transformed)
    print(results)

    print("🔹 Calculating performance metrics...")
    results = calculate_performance(transformed)

    # Optional: save results for dashboard or email alert
    results.to_csv("data/backtest_results.csv", index=False)
    print("✅ Backtest completed and saved!")
