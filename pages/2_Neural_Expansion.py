import streamlit as st
from data.fetch_polygon import get_price_data
from features.indicators import apply_indicators

def render_tab2(ticker):
    st.header("🧠 Neural Expansion: Pulse & Symbolic Insight")

    df = get_price_data(ticker)
    df = apply_indicators(df)

    # MACD Pulse
    st.subheader("🔥 MACD Pulse (Fire Element)")
    st.line_chart(df[["macd", "macd_signal"]])
    st.caption("Fire reveals momentum ignition and exhaustion. MACD histogram reflects the breath of trend energy.")

    # RSI Breath
    st.subheader("🌬️ RSI Breath (Air Element)")
    st.line_chart(df["rsi"])
    rsi_latest = df["rsi"].iloc[-1]
    if rsi_latest > 70:
        st.markdown("**Agni Surge**: RSI above 70 — emotional saturation, possible reversal.")
    elif rsi_latest < 30:
        st.markdown("**Vayu Retreat**: RSI below 30 — oversold, potential rebound.")
    else:
        st.markdown("**Equilibrium Drift**: RSI in neutral zone — breath is steady.")

    # Volatility Tremor
    st.subheader("🌊 Volatility Tremor (Water Element)")
    st.line_chart(df["volatility"])
    st.caption("Water reflects turbulence. Volatility surges signal emotional ripples in market psyche.")

    # Symbolic Summary
    st.markdown("---")
    st.markdown("🔗 **Symbolic Commentary**")
    st.markdown("""
    - **MACD (Fire)**: Tracks ignition and burnout of trend energy.
    - **RSI (Air)**: Measures breath and emotional saturation.
    - **Volatility (Water)**: Reveals tremors and uncertainty.
    Together, they form a pulse map of collective sentiment and elemental balance.
    """)

# import streamlit as st
# from fetch_polygon import get_price_data
# from indicators import apply_indicators

# def render_tab2(ticker):
#     st.header("🧠 Neural Expansion: Pulse & Symbolic Insight")

#     df = get_price_data(ticker)
#     df = apply_indicators(df)

#     st.subheader("📈 MACD Pulse")
#     st.line_chart(df[["macd", "macd_signal"]])

#     st.subheader("🌬️ RSI Breath")
#     st.line_chart(df["rsi"])

#     st.subheader("🌊 Volatility Tremor")
#     st.line_chart(df["volatility"])

#     st.caption("Symbolic Commentary: MACD reveals momentum shifts, RSI reflects emotional saturation, and volatility echoes market turbulence. Together, they form a pulse map of collective sentiment.")

# import streamlit as st
# from fetch_polygon import get_price_data
# from indicators import apply_indicators

# def render_tab2(ticker):
#     st.header("🧠 Neural Expansion: Pulse & Symbolic Insight")

#     df = get_price_data(ticker)
#     df = apply_indicators(df)

#     # MACD Pulse
#     st.subheader("🔥 MACD Pulse (Fire Element)")
#     st.line_chart(df[["macd", "macd_signal"]])
#     st.caption("Fire reveals momentum ignition and exhaustion. MACD histogram reflects the breath of trend energy.")

#     # RSI Breath
#     st.subheader("🌬️ RSI Breath (Air Element)")
#     st.line_chart(df["rsi"])
#     rsi_latest = df["rsi"].iloc[-1]
#     if rsi_latest > 70:
#         st.markdown("**Agni Surge**: RSI above 70 — emotional saturation, possible reversal.")
#     elif rsi_latest < 30:
#         st.markdown("**Vayu Retreat**: RSI below 30 — oversold, potential rebound.")
#     else:
#         st.markdown("**Equilibrium Drift**: RSI in neutral zone — breath is steady.")

#     # Volatility Tremor
#     st.subheader("🌊 Volatility Tremor (Water Element)")
#     st.line_chart(df["volatility"])
#     st.caption("Water reflects turbulence. Volatility surges signal emotional ripples in market psyche.")

#     # Symbolic Summary
#     st.markdown("---")
#     st.markdown("🔗 **Symbolic Commentary**")
#     st.markdown("""
#     - **MACD (Fire)**: Tracks ignition and burnout of trend energy.
#     - **RSI (Air)**: Measures breath and emotional saturation.
#     - **Volatility (Water)**: Reveals tremors and uncertainty.
#     Together, they form a pulse map of collective sentiment and elemental balance.
#     """)
