import requests
import pandas as pd
import datetime
import streamlit as st
from utils.key_manager import get_polygon_key, get_alphavantage_key

POLYGON_API_KEY = get_polygon_key()
ALPHAVANTAGE_API_KEY = get_alphavantage_key()

@st.cache_data
def get_price_data(ticker, days=30):
    try:
        return fetch_polygon_data(ticker, days)
    except Exception as e:
        print(f"⚠️ Polygon failed for {ticker}: {e}")
        log_key_failure(POLYGON_API_KEY, str(e))
        try:
            return fetch_alphavantage_data(ticker)
        except Exception as ae:
            print(f"⚠️ AlphaVantage failed for {ticker}: {ae}")
            log_key_failure(ALPHAVANTAGE_API_KEY, str(ae))
            st.warning(f"⚠️ Live data unavailable for {ticker}. Showing symbolic fallback.")
            return fallback_data(ticker)

def fetch_polygon_data(ticker, days):
    end_date = datetime.datetime.now().date()
    start_date = end_date - datetime.timedelta(days=days)
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&apiKey={POLYGON_API_KEY}"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    if "results" not in data:
        raise ValueError("Polygon returned no results")
    df = pd.DataFrame(data["results"])
    df["date"] = pd.to_datetime(df["t"], unit="ms")
    df.rename(columns={"o": "open", "h": "high", "l": "low", "c": "close", "v": "volume"}, inplace=True)
    return df[["date", "open", "high", "low", "close", "volume"]]

def fetch_alphavantage_data(ticker):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&outputsize=compact&apikey={ALPHAVANTAGE_API_KEY}"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    if "Time Series (Daily)" not in data:
        raise ValueError("AlphaVantage returned no time series")
    ts = data["Time Series (Daily)"]
    df = pd.DataFrame.from_dict(ts, orient="index")
    df.index = pd.to_datetime(df.index)
    df = df.sort_index().tail(30)
    df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "6. volume": "volume"
    }, inplace=True)
    df.reset_index(inplace=True)
    df.rename(columns={"index": "date"}, inplace=True)
    df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)
    return df[["date", "open", "high", "low", "close", "volume"]]

def fallback_data(ticker):
    base = hash(ticker) % 50 + 100
    dates = pd.date_range(end=datetime.datetime.now(), periods=30)
    df = pd.DataFrame({
        "date": dates,
        "open": [base + i for i in range(30)],
        "high": [base + 2 + i for i in range(30)],
        "low": [base - 2 + i for i in range(30)],
        "close": [base + 1 + i for i in range(30)],
        "volume": [1000000 + i * 1000 for i in range(30)]
    })
    return df

def log_key_failure(key, error):
    try:
        with open("logs/key_failures.log", "a") as f:
            f.write(f"{datetime.datetime.now()} | {key} | {error}\n")
    except Exception as log_error:
        print(f"⚠️ Failed to log key error: {log_error}")
