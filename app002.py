import streamlit as st
from components.header import render_header
from components.sector_selector import render_sector_selector
from components.chart_renderer import render_charts
from features.lore_engine import render_lore
from features.log_setup import initialize_logs
from features.style_manager import apply_all_styles  # 🆕 Inject fonts + symbolic CSS

# 🔧 Initialize logging system
initialize_logs()

# 🎨 Apply symbolic styles and fonts
apply_all_styles()

# === Page Config ===
st.set_page_config(
    page_title="Lucy 2 Dashboard",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
