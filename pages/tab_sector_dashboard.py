import streamlit as st
from components.sector_selector import render_sector_selector, get_elemental_mapping,load_sectors
from features.sector_indicators import get_sector_indicators

def render_sector_dashboard():
    st.header("🌐 Sector Dashboard: Elemental Pulse")

    sector, ticker = render_sector_selector()
    elemental = get_elemental_mapping().get(sector, "🌀 Unknown")
    st.markdown(f"**Elemental Archetype**: {elemental}")

    tickers = load_sectors()[sector]
    sector_data = get_sector_indicators(tickers)

    st.subheader("🔥 MACD Pulse Across Sector")
    for tkr, df in sector_data.items():
        st.line_chart(df[["macd", "macd_signal"]], height=150)
        st.caption(f"{tkr}: MACD reveals ignition and exhaustion.")

    st.subheader("🌬️ RSI Breath Across Sector")
    for tkr, df in sector_data.items():
        st.line_chart(df["rsi"], height=150)
        rsi = df["rsi"].iloc[-1]
        if rsi > 70:
            st.markdown(f"{tkr}: **Agni Surge**")
        elif rsi < 30:
            st.markdown(f"{tkr}: **Vayu Retreat**")
        else:
            st.markdown(f"{tkr}: **Equilibrium Drift**")

    st.subheader("🌊 Volatility Tremor Across Sector")
    for tkr, df in sector_data.items():
        st.line_chart(df["volatility"], height=150)
        st.caption(f"{tkr}: Volatility reflects emotional ripples.")
