import datetime
import streamlit as st
from utils.config import ENABLE_ELEMENTAL_OVERLAYS, ENABLE_LORE_ENGINE, ENABLE_BREATH_ANIMATION

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
    keys = [k for k in keys if k]
    return get_api_keys().get("POLYGON_API_KEY", get_rotating_key(keys))

# === AlphaVantage Key Access ===
def get_alphavantage_key():
    keys = [
        get_api_keys().get("ALPHAVANTAGE_API_KEY1"),
        get_api_keys().get("ALPHAVANTAGE_API_KEY2")
    ]
    keys = [k for k in keys if k]
    return get_api_keys().get("ALPHAVANTAGE_API_KEY", get_rotating_key(keys))

# === Config Logger ===
def log_config_state():
    api_keys = get_api_keys()

    def mask(key):
        return key[:6] + "..." if key else "missing"

    polygon_keys = [
        mask(api_keys.get("POLYGON_API_KEY")),
        mask(api_keys.get("POLYGON_API_KEY1")),
        mask(api_keys.get("POLYGON_API_KEY2"))
    ]

    alphavantage_keys = [
        mask(api_keys.get("ALPHAVANTAGE_API_KEY")),
        mask(api_keys.get("ALPHAVANTAGE_API_KEY1")),
        mask(api_keys.get("ALPHAVANTAGE_API_KEY2"))
    ]

    st.write("🔐 **API Key Status**")
    st.write(f"Polygon Keys: {polygon_keys}")
    st.write(f"AlphaVantage Keys: {alphavantage_keys}")

    st.write("🧠 **Symbolic Toggles**")
    st.write(f"Elemental Overlays: {ENABLE_ELEMENTAL_OVERLAYS}")
    st.write(f"Lore Engine: {ENABLE_LORE_ENGINE}")
    st.write(f"Breath Animation: {ENABLE_BREATH_ANIMATION}")
