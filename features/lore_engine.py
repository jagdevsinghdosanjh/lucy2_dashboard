import streamlit as st
import html
from config.symbols import GURUBANI_OVERLAYS, ELEMENTAL_MAP

def get_lore_text(ticker, indicator_type="RSI", value=None):
    safe_ticker = html.escape(ticker)
    overlay = GURUBANI_OVERLAYS.get(indicator_type, "")
    element = ELEMENTAL_MAP.get("Technology", "🌐")  # Default or dynamic sector mapping

    # Base poetic lore
    base_lore = f"""
    <div class='lore-text'>
        {element} <strong>{safe_ticker}</strong> breathes through Fibonacci spirals, echoing the cellular memory of price.<br>
        Each retracement is a whisper from the past, each extension a leap into symbolic cognition.<br>
        <em>{overlay}</em>
    </div>
    """

    # New feature: dynamic commentary based on indicator
    if indicator_type == "RSI" and value is not None:
        if value > 70:
            base_lore += "<div class='lore-hint'>🔥 Overbought: The pulse quickens, nearing the edge of exuberance.</div>"
        elif value < 30:
            base_lore += "<div class='lore-hint'>💧 Oversold: The breath slows, echoing a descent into reflection.</div>"
    elif indicator_type == "MACD" and value is not None:
        if value > 0:
            base_lore += "<div class='lore-hint'>⚡ Momentum rising: The signal surges with directional clarity.</div>"
        else:
            base_lore += "<div class='lore-hint'>🌫️ Momentum fading: Divergence whispers of reversal.</div>"
    elif indicator_type == "VIX" and value is not None:
        if value > 25:
            base_lore += "<div class='lore-hint'>🌪️ Volatility high: The breath trembles in uncertainty.</div>"
        else:
            base_lore += "<div class='lore-hint'>🌤️ Calm winds: The breath steadies in quiet anticipation.</div>"

    return base_lore

def render_lore(ticker, indicator_type="RSI", value=None):
    if not ticker:
        return
    st.markdown("""
        <style>
        .lore-text { font-family: 'Georgia'; font-size: 1.1rem; color: #00ffe0; margin-bottom: 10px; }
        .lore-hint { font-family: 'Courier New'; font-size: 0.95rem; color: #ffcc00; margin-top: 5px; }
        </style>
    """, unsafe_allow_html=True)
    st.markdown(get_lore_text(ticker, indicator_type, value), unsafe_allow_html=True)

# import streamlit as st

# def render_lore(ticker):
#     st.markdown(f"<div class='lore-text'>🧬{ticker} pulses through the neural grid, echoing the breath of Fibonacci and the rhythm of cosmic cycles.
#                 </div>", unsafe_allow_html=True)
# # def render_lore(ticker):
#     st.markdown(f"""
#         <div class='lore-text'>{ticker} breathes through Fibonacci spirals, echoing the cellular memory of price. 
#         Each retracement is a whisper from the past, each extension a leap into symbolic cognition.
#         </div>
#     """, unsafe_allow_html=True)
