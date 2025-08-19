import streamlit as st
import plotly.graph_objects as go
from features.fetch_polygon import get_price_data

def render_charts(ticker):
    st.markdown(f"### 📈 Charts for {ticker}")
    df = get_price_data(ticker)

    if df.empty:
        st.warning("No data available to render chart.")
        return

    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df["date"],
        open=df["open"],
        high=df["high"],
        low=df["low"],
        close=df["close"],
        name="Price"
    ))

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price",
        xaxis_rangeslider_visible=False,
        template="plotly_dark",
        height=500,
        margin=dict(t=40, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)
