import streamlit as st
import time
import random

def show_startup_animation():
    metaphors = [
        "Breath becomes geometry",
        "The dashboard dreams in Fibonacci",
        "From silence, the pulse emerges",
        "Each sector is a syllable of the cosmic poem",
        "Lucy 2 awakens the elemental code"
    ]
    chosen_metaphor = random.choice(metaphors)

    st.markdown(f"""
        <style>
        .lucy-container {{
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background-color: #0F0F0F;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            animation: fadeOut 3s ease-in-out 3s forwards;
        }}

        .lucy-text {{
            font-size: 2.8em;
            color: #FF6F61;
            font-family: 'sans-serif';
            text-align: center;
            animation: pulse 3s infinite;
        }}

        .glyph {{
            position: absolute;
            font-size: 4em;
            opacity: 0.2;
            animation: orbit 6s linear infinite;
        }}

        .glyph.fire {{ top: 20%; left: 15%; color: #FF4500; }}
        .glyph.water {{ top: 70%; left: 20%; color: #00BFFF; }}
        .glyph.air {{ top: 30%; right: 15%; color: #D3D3D3; }}
        .glyph.earth {{ bottom: 10%; right: 25%; color: #8B4513; }}

        @keyframes pulse {{
            0% {{ transform: scale(1); opacity: 0.6; }}
            50% {{ transform: scale(1.1); opacity: 1; }}
            100% {{ transform: scale(1); opacity: 0.6; }}
        }}

        @keyframes fadeOut {{
            to {{ opacity: 0; visibility: hidden; }}
        }}

        @keyframes orbit {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
        </style>

        <div class="lucy-container">
            <div class="lucy-text">{chosen_metaphor}</div>
            <div class="glyph fire">🔥</div>
            <div class="glyph water">💧</div>
            <div class="glyph air">🌬️</div>
            <div class="glyph earth">🌍</div>
        </div>
    """, unsafe_allow_html=True)

    time.sleep(4)
