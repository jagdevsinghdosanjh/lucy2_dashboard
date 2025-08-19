import pandas as pd

def compute_fibonacci_levels(df):
    high = df['high'].max()
    low = df['low'].min()
    diff = high - low
    levels = {
        "0.0%": low,
        "23.6%": high - 0.236 * diff,
        "38.2%": high - 0.382 * diff,
        "50.0%": high - 0.5 * diff,
        "61.8%": high - 0.618 * diff,
        "100.0%": high
    }
    return levels

def calculate_macd(df, fast=12, slow=26, signal=9):
    df["ema_fast"] = df["close"].ewm(span=fast, adjust=False).mean()
    df["ema_slow"] = df["close"].ewm(span=slow, adjust=False).mean()
    df["macd"] = df["ema_fast"] - df["ema_slow"]
    df["macd_signal"] = df["macd"].ewm(span=signal, adjust=False).mean()
    df["macd_histogram"] = df["macd"] - df["macd_signal"]
    return df

def calculate_rsi(df, period=14):
    delta = df["close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    df["rsi"] = 100 - (100 / (1 + rs))
    return df

def calculate_volatility(df, window=10):
    df["volatility"] = df["close"].rolling(window=window).std()
    return df

def apply_indicators(df):
    df = calculate_macd(df)
    df = calculate_rsi(df)
    df = calculate_volatility(df)
    return df
