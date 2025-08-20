import datetime
import streamlit as st

# === API Key Rotation Logic ===
def get_rotating_key(key_list):
    day = datetime.datetime.now().day
    return key_list[day % len(key_list)]

# === Polygon Keys ===
POLYGON_KEYS = [
    st.secrets["api_keys"].get("POLYGON_API_KEY1", "Qr1E6i3PdteQk1HEVF8TmCDqPqXLknwn"),
    st.secrets["api_keys"].get("POLYGON_API_KEY2", "kaUZ2wiN5pUFJVudYr8f_s1Gao3dp5y2")
]

# === AlphaVantage Keys ===
ALPHAVANTAGE_KEYS = [
    st.secrets["api_keys"].get("ALPHAVANTAGE_API_KEY1", "demo"),
    st.secrets["api_keys"].get("ALPHAVANTAGE_API_KEY2", "your-second-alphavantage-key")
]

# === Final Key Selection ===
POLYGON_API_KEY = st.secrets["api_keys"].get("POLYGON_API_KEY", get_rotating_key(POLYGON_KEYS))
ALPHAVANTAGE_API_KEY = st.secrets["api_keys"].get("ALPHAVANTAGE_API_KEY", get_rotating_key(ALPHAVANTAGE_KEYS))

# === Feature Toggles ===
ENABLE_ELEMENTAL_OVERLAYS = st.secrets["features"].get("ENABLE_ELEMENTAL_OVERLAYS", False)
ENABLE_LORE_ENGINE = st.secrets["features"].get("ENABLE_LORE_ENGINE", True)
ENABLE_BREATH_ANIMATION = st.secrets["features"].get("ENABLE_BREATH_ANIMATION", True)

# === Optional Logging Message ===
def log_config_state():
    print(f"🔑 Polygon Key: {POLYGON_API_KEY[:6]}... | AlphaVantage Key: {ALPHAVANTAGE_API_KEY[:6]}...")
    print(f"✨ Elemental Overlays: {ENABLE_ELEMENTAL_OVERLAYS} | Lore Engine: {ENABLE_LORE_ENGINE} | Breath Animation: {ENABLE_BREATH_ANIMATION}")
