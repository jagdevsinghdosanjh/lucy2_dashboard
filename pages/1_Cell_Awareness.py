import streamlit as st
from data.fetch_polygon import get_price_data
from features.indicators import compute_fibonacci_levels
from features.overlays import render_fractal_overlay
from features.lore_engine import render_lore
import plotly.graph_objects as go

st.set_page_config(page_title="Cellular Awareness", layout="wide")

# === Header ===
st.markdown("<div class='header'>🧬 Cellular Awareness</div>", unsafe_allow_html=True)

# === Company Selector ===
ticker = st.selectbox("Choose a company", ["AAPL", "MSFT", "GOOGL", "TSLA"])

# === Fetch Price Data ===
df = get_price_data(ticker)

# === Compute Fibonacci Levels ===
fib_levels = compute_fibonacci_levels(df)

# === Plot Chart ===
fig = go.Figure()
fig.add_trace(go.Candlestick(
    x=df['date'],
    open=df['open'],
    high=df['high'],
    low=df['low'],
    close=df['close'],
    name="Price"
))

# Add Fibonacci lines
for level, price in fib_levels.items():
    fig.add_hline(y=price, line_dash="dot", annotation_text=f"{level}: {price:.2f}", line_color="#FFD700")

# Add fractal overlay
render_fractal_overlay(fig, df)

st.plotly_chart(fig, use_container_width=True)

# === Lore Commentary ===
render_lore(ticker)
