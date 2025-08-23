import streamlit.components.v1 as components

# Dynamic indicator values (replace with real-time data as needed)
vix = 18
rsi = 65
macd = 1.2
macd_signal = 0.8

# HTML + JS + CSS block
html_code = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Dashboard Pulse</title>
    <script>
      window.vix = {vix};
      window.rsi = {rsi};
      window.macd = {macd};
      window.macdSignal = {macd_signal};
    </script>
    <script src="logo_pulse.js"></script>
    <style>
      body {{
        font-family: 'Segoe UI', sans-serif;
        color: #ffffff;
        background-color: #0f0f0f;
        text-align: center;
        padding-top: 20px;
      }}
      #logo {{
        width: 140px;
        animation: breath 4s ease-in-out infinite;
        filter: drop-shadow(0 0 10px #00ffe0);
      }}
      @keyframes breath {{
        0% {{ transform: scale(1); opacity: 0.9; }}
        50% {{ transform: scale(1.15); opacity: 1; }}
        100% {{ transform: scale(1); opacity: 0.9; }}
      }}
    </style>
  </head>
  <body>
    <h2>Welcome to <span style="color:#00ffe0;">Dashboard Pulse</span></h2>
    <img id="logo" src="./lucy_logo_card.png" alt="Lucy Logo" />
  </body>
</html>
"""

# Render the HTML component
components.html(html_code, height=320)
