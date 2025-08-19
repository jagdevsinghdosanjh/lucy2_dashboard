import streamlit as st
from components.header import render_header
from components.sector_selector import render_sector_selector
from components.chart_renderer import render_charts
from features.lore_engine import render_lore
from features.log_setup import initialize_logs

# 🔧 Initialize logging system
initialize_logs()


# === Page Config ===
st.set_page_config(
    page_title="Lucy 2 Dashboard",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === Load Custom CSS & Fonts ===
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500&family=Cinzel+Decorative&display=swap" rel="stylesheet">
    <style>
        @import url('assets/styles.css');
    </style>
""", unsafe_allow_html=True)

# === Header Banner ===
render_header("Lucy 2: Symbolic Market Dashboard")

# === Sidebar Sector Selector ===
with st.sidebar:
    selected_sector, selected_company = render_sector_selector()

# === Main Dashboard ===
st.markdown("## 📊 Market Pulse")
render_charts(selected_company)

# === Lore Overlay ===
st.markdown("---")
render_lore(selected_company)
