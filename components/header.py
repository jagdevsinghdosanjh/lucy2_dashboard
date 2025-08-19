import streamlit as st

def render_header(title):
    st.markdown(f"<div class='header'>{title}</div>", unsafe_allow_html=True)
