import os
import datetime
import streamlit as st

# === Secure Secrets Access ===
api_keys = st.secrets.get("api_keys", {})
features = st.secrets.get("features", {})

# === Load Keys Securely ===
POLYGON_KEYS = api_keys.get("POLYGON_API_KEYS", os.getenv("POLYGON_API_KEYS", "")).split(",")
ALPHAVANTAGE_KEYS = api_keys.get("ALPHAVANTAGE_API_KEYS", os.getenv("ALPHAVANTAGE_API_KEYS", "")).split(",")

# === Rotation Strategy ===
def get_rotating_key(key_list):
    if not key_list:
        return None
    day = datetime.datetime.now().day
    return key_list[day % len(key_list)]

# === Final Key Selection ===
POLYGON_API_KEY = api_keys.get("POLYGON_API_KEY", get_rotating_key(POLYGON_KEYS))
ALPHAVANTAGE_API_KEY = api_keys.get("ALPHAVANTAGE_API_KEY", get_rotating_key(ALPHAVANTAGE_KEYS))

# === Feature Toggles ===
ENABLE_ELEMENTAL_OVERLAYS = features.get("ENABLE_ELEMENTAL_OVERLAYS", False)
ENABLE_LORE_ENGINE = features.get("ENABLE_LORE_ENGINE", True)
ENABLE_BREATH_ANIMATION = features.get("ENABLE_BREATH_ANIMATION", True)

# === Optional Logging Message ===
def log_config_state():
    print(f"🔑 Polygon Key: {POLYGON_API_KEY[:6]}... | AlphaVantage Key: {ALPHAVANTAGE_API_KEY[:6]}...")
    print(f"✨ Elemental Overlays: {ENABLE_ELEMENTAL_OVERLAYS} | Lore Engine: {ENABLE_LORE_ENGINE} | Breath Animation: {ENABLE_BREATH_ANIMATION}")
