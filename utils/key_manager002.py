import os
import datetime
import streamlit as st

def get_polygon_key():
    return st.secrets.get("api_keys", {}).get("POLYGON_API_KEY1", "fallback_key")

def get_alphavantage_key():
    return st.secrets.get("api_keys", {}).get("ALPHAVANTAGE_API_KEY1", "fallback_key")


# === Define Your Keys ===
POLYGON_KEYS = [
    st.secrets["api_keys"].get("POLYGON_API_KEY1", "Qr1E6i3PdteQk1HEVF8TmCDqPqXLknwn"),
    st.secrets["api_keys"].get("POLYGON_API_KEY2", "kaUZ2wiN5pUFJVudYr8f_s1Gao3dp5y2")
]

ALPHAVANTAGE_KEYS = [
    st.secrets["api_keys"].get("ALPHAVANTAGE_API_KEY1", "demo"),
    st.secrets["api_keys"].get("ALPHAVANTAGE_API_KEY2", "your-second-alphavantage-key")
]

# === Rotation Strategy ===
def get_rotating_key(key_list):
    day = datetime.datetime.now().day
    return key_list[day % len(key_list)]

# === Polygon Key Access ===
def get_polygon_key():
    return st.secrets["api_keys"].get("POLYGON_API_KEY", get_rotating_key(POLYGON_KEYS))

# === AlphaVantage Key Access ===
def get_alphavantage_key():
    return st.secrets["api_keys"].get("ALPHAVANTAGE_API_KEY", get_rotating_key(ALPHAVANTAGE_KEYS))
