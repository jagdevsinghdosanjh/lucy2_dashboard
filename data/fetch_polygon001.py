import requests
import pandas as pd
import datetime
from utils.key_manager import get_polygon_key

POLYGON_API_KEY = get_polygon_key()

def get_price_data(ticker, days=30):
    end_date = datetime.datetime.now().date()
    start_date = end_date - datetime.timedelta(days=days)

    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&apiKey={POLYGON_API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "results" not in data:
            raise ValueError("No results found")

        df = pd.DataFrame(data["results"])
        df["date"] = pd.to_datetime(df["t"], unit="ms")
        df.rename(columns={"o": "open", "h": "high", "l": "low", "c": "close", "v": "volume"}, inplace=True)
        return df[["date", "open", "high", "low", "close", "volume"]]

    except Exception as e:
        print(f"⚠️ Polygon API error: {e}")
        log_key_failure(POLYGON_API_KEY, str(e))
        return fallback_data(ticker)

def log_key_failure(key, error):
    try:
        with open("logs/key_failures.log", "a") as f:
            f.write(f"{datetime.datetime.now()} | {key} | {error}\n")
    except Exception as log_error:
        print(f"⚠️ Failed to log key error: {log_error}")

def fallback_data(ticker):
    dates = pd.date_range(end=datetime.datetime.now(), periods=30)
    df = pd.DataFrame({
        "date": dates,
        "open": [100 + i for i in range(30)],
        "high": [102 + i for i in range(30)],
        "low": [98 + i for i in range(30)],
        "close": [101 + i for i in range(30)],
        "volume": [1000000 + i * 1000 for i in range(30)]
    })
    return df

# import requests
# import pandas as pd
# import os
# import datetime
# from utils.key_manager import get_polygon_key

# POLYGON_API_KEY = get_polygon_key()

# # === Load API Key ===
# POLYGON_API_KEY = os.getenv("POLYGON_API_KEY", "your_fallback_key_here")

# def get_price_data(ticker, days=30):
#     end_date = datetime.datetime.now().date()
#     start_date = end_date - datetime.timedelta(days=days)

#     url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&apiKey={POLYGON_API_KEY}"

#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()

#         if "results" not in data:
#             raise ValueError("No results found")

#         df = pd.DataFrame(data["results"])
#         df["date"] = pd.to_datetime(df["t"], unit="ms")
#         df.rename(columns={"o": "open", "h": "high", "l": "low", "c": "close", "v": "volume"}, inplace=True)
#         return df[["date", "open", "high", "low", "close", "volume"]]

#     except Exception as e:
#         print(f"⚠️ Polygon API error: {e}")
#         return fallback_data(ticker)
#     def log_key_failure(key, error):
#     with open("logs/key_failures.log", "a") as f:
#         f.write(f"{datetime.datetime.now()} | {key} | {error}\n")


# def fallback_data(ticker):
#     # Simulated fallback data (can be replaced with local cache or static CSV)
#     dates = pd.date_range(end=datetime.datetime.now(), periods=30)
#     df = pd.DataFrame({
#         "date": dates,
#         "open": [100 + i for i in range(30)],
#         "high": [102 + i for i in range(30)],
#         "low": [98 + i for i in range(30)],
#         "close": [101 + i for i in range(30)],
#         "volume": [1000000 + i * 1000 for i in range(30)]
#     })
#     return df
