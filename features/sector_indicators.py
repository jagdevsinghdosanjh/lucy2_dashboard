from data.fetch_polygon import get_price_data
from features.indicators import apply_indicators

def get_sector_indicators(tickers):
    sector_data = {}
    for ticker in tickers:
        try:
            df = get_price_data(ticker)
            df = apply_indicators(df)
            sector_data[ticker] = df
        except Exception as e:
            print(f"⚠️ Failed to process {ticker}: {e}")
    return sector_data
