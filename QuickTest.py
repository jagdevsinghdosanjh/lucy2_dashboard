import os
from dotenv import load_dotenv

load_dotenv()

print("Polygon Key:", os.getenv("POLYGON_API_KEY"))
print("AlphaVantage Key:", os.getenv("ALPHAVANTAGE_API_KEY"))
print("Elemental Overlays Enabled:", os.getenv("ENABLE_ELEMENTAL_OVERLAYS"))
