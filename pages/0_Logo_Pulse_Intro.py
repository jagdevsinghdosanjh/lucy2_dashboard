import streamlit.components.v1 as components

# Example dynamic values (replace with real-time indicators)
vix = 18
rsi = 65
macd = 1.2
macd_signal = 0.8

html_code = f"""
<html>
  <head>
    <script>
      window.vix = {vix};
      window.rsi = {rsi};
      window.macd = {macd};
      window.macdSignal = {macd_signal};
    </script>
    <script src="logo_pulse.js"></script>
    <style>
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
    <img src="lucy_logo_card.png" id="logo" />
  </body>
</html>
"""

components.html(html_code, height=300)

# import streamlit.components.v1 as components

# components.html(open("public/logo_pulse.html").read(), height=300)
