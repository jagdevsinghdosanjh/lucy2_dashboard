import streamlit as st
import time

def show_startup_animation():
    st.markdown("""
        <style>
        .lucy-container {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background-color: #0F0F0F;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            animation: fadeOut 3s ease-in-out 3s forwards;
        }

        .lucy-text {
            font-size: 3em;
            color: #FF6F61;
            font-family: 'sans-serif';
            text-align: center;
            animation: pulse 3s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); opacity: 0.6; }
            50% { transform: scale(1.1); opacity: 1; }
            100% { transform: scale(1); opacity: 0.6; }
        }

        @keyframes fadeOut {
            to { opacity: 0; visibility: hidden; }
        }
        </style>

        <div class="lucy-container">
            <div class="lucy-text">Lucy 2 Awakens...</div>
        </div>
    """, unsafe_allow_html=True)

    # Optional delay to allow animation before dashboard loads
    time.sleep(4)
