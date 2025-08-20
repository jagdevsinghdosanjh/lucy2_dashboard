import os
import datetime
import random # noqa

# === Define Your Keys ===
POLYGON_KEYS = [
    "Qr1E6i3PdteQk1HEVF8TmCDqPqXLknwn",
    "kaUZ2wiN5pUFJVudYr8f_s1Gao3dp5y2"
]

ALPHAVANTAGE_KEYS = [
    "demo",  # Replace with real keys
    "your-second-alphavantage-key"
]

# === Rotation Strategy ===
def get_rotating_key(key_list):
    day = datetime.datetime.now().day
    return key_list[day % len(key_list)]
    # Or use: return random.choice(key_list)

# === Polygon Key Access ===
def get_polygon_key():
    return os.getenv("POLYGON_API_KEY", get_rotating_key(POLYGON_KEYS))

# === AlphaVantage Key Access ===
def get_alphavantage_key():
    return os.getenv("ALPHAVANTAGE_API_KEY", get_rotating_key(ALPHAVANTAGE_KEYS))
