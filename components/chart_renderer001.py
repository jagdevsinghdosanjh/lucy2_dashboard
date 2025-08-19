import streamlit as st
import plotly.graph_objects as go

def render_charts(ticker):
    st.markdown(f"### 📈 Charts for {ticker}")
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=["2025-08-18", "2025-08-19"],
        open=[100, 102],
        high=[105, 106],
        low=[98, 99],
        close=[104, 103]
    ))
    st.plotly_chart(fig, use_container_width=True)
