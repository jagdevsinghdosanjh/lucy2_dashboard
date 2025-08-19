import streamlit as st
import json
import pandas as pd

def load_sectors(source="data/sectors.json"):
    if source.endswith(".json"):
        with open(source, "r") as f:
            sectors = json.load(f)
    elif source.endswith(".csv"):
        df = pd.read_csv(source)
        sectors = df.groupby("Sector")["Ticker"].apply(list).to_dict()
    else:
        raise ValueError("Unsupported file format")
    return sectors

def get_elemental_mapping():
    return {
        "Energy": "🔥 Fire",
        "Technology": "🌬️ Air",
        "Healthcare": "🌊 Water",
        "Finance": "🪨 Earth",
        "Consumer": "🌱 Growth",
        "Utilities": "⚡ Ether"
    }

def get_sector_dropdown(sectors):
    return list(sectors.keys())

def render_sector_selector(source="data/sectors.json"):
    sectors = load_sectors(source)
    elemental = get_elemental_mapping()

    selected_sector = st.selectbox("Select Sector", get_sector_dropdown(sectors))
    st.markdown(f"**Elemental Archetype**: {elemental.get(selected_sector, '🌀 Unknown')}")

    selected_company = st.selectbox("Select Company", sectors[selected_sector])
    return selected_sector, selected_company

# import streamlit as st
# import json
# import pandas as pd

# def render_sector_selector():
#     sectors = {
#         "Technology": ["AAPL", "MSFT", "GOOGL"],
#         "Healthcare": ["JNJ", "PFE", "MRNA"],
#         "Energy": ["XOM", "CVX", "BP"]
#     }
#     selected_sector = st.selectbox("Select Sector", list(sectors.keys()))
#     selected_company = st.selectbox("Select Company", sectors[selected_sector])
#     return selected_sector, selected_company


# def load_sectors(source="data/sectors.json"):
#     if source.endswith(".json"):
#         with open(source, "r") as f:
#             sectors = json.load(f)
#     elif source.endswith(".csv"):
#         df = pd.read_csv(source)
#         sectors = df.groupby("Sector")["Ticker"].apply(list).to_dict()
#     else:
#         raise ValueError("Unsupported file format")
#     return sectors

# import json
# import pandas as pd

# def load_sectors(source="data/sectors.json"):
#     if source.endswith(".json"):
#         with open(source, "r") as f:
#             sectors = json.load(f)
#     elif source.endswith(".csv"):
#         df = pd.read_csv(source)
#         sectors = df.groupby("Sector")["Ticker"].apply(list).to_dict()
#     else:
#         raise ValueError("Unsupported file format")
#     return sectors

# def get_elemental_mapping():
#     return {
#         "Energy": "🔥 Fire",
#         "Technology": "🌬️ Air",
#         "Healthcare": "🌊 Water",
#         "Finance": "🪨 Earth",
#         "Consumer": "🌱 Growth",
#         "Utilities": "⚡ Ether"
#     }

# def get_sector_dropdown(sectors):
#     return list(sectors.keys())
