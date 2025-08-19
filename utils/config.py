import os
import datetime

# Hardcoded keys (optional fallback)
POLYGON_API_KEY1 = "Qr1E6i3PdteQk1HEVF8TmCDqPqXLknwn"
POLYGON_API_KEY2 = "kaUZ2wiN5pUFJVudYr8f_s1Gao3dp5y2"

# Try environment variable first
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

# If not set, fallback to key 1
if not POLYGON_API_KEY:
    POLYGON_API_KEY = POLYGON_API_KEY1

def get_rotating_key():
    day = datetime.datetime.now().day
    return POLYGON_API_KEY1 if day % 2 == 0 else POLYGON_API_KEY2

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY", get_rotating_key())

# POLYGON_API_KEY1="Qr1E6i3PdteQk1HEVF8TmCDqPqXLknwn"
# POLYGON_API_KEY2="kaUZ2wiN5pUFJVudYr8f_s1Gao3dp5y2"

# import os

# POLYGON_API_KEY = os.getenv("POLYGON_API_KEY", "your_fallback_key_here")
