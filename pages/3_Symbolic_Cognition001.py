import streamlit as st
from config import (
    POLYGON_API_KEY,
    ALPHAVANTAGE_API_KEY,
    ENABLE_ELEMENTAL_OVERLAYS,
    ENABLE_LORE_ENGINE,
    ENABLE_BREATH_ANIMATION,
    log_config_state
)

def config_card():
    st.markdown("## 🧠 Symbolic Cognition Settings")
    st.markdown("Tune Lucy 2’s expressive breath and overlays:")

    st.toggle("🌌 Elemental Overlays", value=ENABLE_ELEMENTAL_OVERLAYS, disabled=True, help="Infuse sector tabs with elemental archetypes")
    st.toggle("📜 Lore Engine", value=ENABLE_LORE_ENGINE, disabled=True, help="Render poetic commentary based on indicators")
    st.toggle("💨 Breath Animation", value=ENABLE_BREATH_ANIMATION, disabled=True, help="Animate UI elements based on RSI and cycles")

    st.markdown("---")
    st.markdown("### 🔑 API Key Status")
    st.code(f"Polygon Key: {POLYGON_API_KEY[:6]}... (rotating)\nAlphaVantage Key: {ALPHAVANTAGE_API_KEY[:6]}... (rotating)", language="text")

    st.markdown("### ✨ Symbolic Commentary")
    st.markdown("""
    - **Elemental Overlays** awaken the dashboard’s mythic anatomy.
    - **Lore Engine** listens to the pulse of price and whispers metaphors.
    - **Breath Animation** synchronizes geometry with market emotion.
    """)

    log_config_state()

# === Render the Config Card ===
config_card()
