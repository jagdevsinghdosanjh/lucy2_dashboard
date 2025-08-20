import datetime
import streamlit as st

# === Safe Access to Secrets ===
def get_api_keys():
    return st.secrets.get("api_keys", {})

# === Rotation Strategy ===
def get_rotating_key(keys):
    if not keys:
        return "fallback_key"
    day = datetime.datetime.now().day
    return keys[day % len(keys)]

# === Polygon Key Access ===
def get_polygon_key():
    keys = [
        get_api_keys().get("POLYGON_API_KEY1"),
        get_api_keys().get("POLYGON_API_KEY2")
    ]
    keys = [k for k in keys if k]  # Filter out None
    return get_api_keys().get("POLYGON_API_KEY", get_rotating_key(keys))

# === AlphaVantage Key Access ===
def get_alphavantage_key():
    keys = [
        get_api_keys().get("ALPHAVANTAGE_API_KEY1"),
        get_api_keys().get("ALPHAVANTAGE_API_KEY2")
    ]
    keys = [k for k in keys if k]
    return get_api_keys().get("ALPHAVANTAGE_API_KEY", get_rotating_key(keys))
