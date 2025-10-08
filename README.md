
# Automated Financial Analytics & Forecasting System

This project is an end-to-end, open-source quantitative pipeline that ingests daily market data, engineers technical features, runs backtests and forecasts, and exposes results via a Streamlit dashboard.

Features:
- Daily ETL that fetches price data (yfinance) and stores it in DuckDB.
- Feature enrichment: MA50/MA200, signals, returns, cumulative performance.
- Backtesting engine that computes strategy performance (cumulative return, Sharpe).
- Forecasting via Prophet with per-ticker predictions and uncertainty bands.
- Automation: scheduled runs and commits via GitHub Actions; email alerts for signals.
- Live dashboard deployed on Streamlit Community Cloud.

See `/app/dashboard.py` for the dashboard and `/src` for ETL, backtest, and forecast code.
