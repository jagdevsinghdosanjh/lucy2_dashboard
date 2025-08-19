import streamlit as st

def inject_fonts():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro&family=Spectral&display=swap" rel="stylesheet">
        <style>
        body {
            font-family: 'Spectral', serif;
        }
        </style>
    """, unsafe_allow_html=True)

def inject_symbolic_styles():
    st.markdown("""
        <style>
        .symbolic-commentary {
            font-family: 'Crimson Pro', serif;
            font-size: 1.1rem;
            color: #FF4500;
            background-color: #fdf6e3;
            padding: 12px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0 0 10px rgba(255, 69, 0, 0.2);
        }

        .fallback-notice {
            font-family: 'Spectral', serif;
            font-size: 0.95rem;
            color: #B22222;
            background-color: #fff0f0;
            padding: 8px;
            border-left: 4px solid #B22222;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

def apply_all_styles():
    inject_fonts()
    inject_symbolic_styles()
