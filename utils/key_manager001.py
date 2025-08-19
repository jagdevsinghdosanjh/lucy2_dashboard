import os
import datetime
import random

# === Define Your Keys ===
API_KEYS = [
    "Qr1E6i3PdteQk1HEVF8TmCDqPqXLknwn",
    "kaUZ2wiN5pUFJVudYr8f_s1Gao3dp5y2"
]

# === Rotation Strategy ===
def get_rotating_key():
    # Option 1: Alternate daily
    day = datetime.datetime.now().day
    return API_KEYS[day % len(API_KEYS)]

    # Option 2: Random fallback
    # return random.choice(API_KEYS)

# === Environment Override ===
def get_polygon_key():
    return os.getenv("POLYGON_API_KEY", get_rotating_key())
