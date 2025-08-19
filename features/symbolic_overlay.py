import os
import json

# 🔮 Load elemental archetypes mapped to sectors
def load_elemental_mappings(filepath="data/elemental_mappings.json"):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Failed to load elemental mappings: {e}")
        return {}

# 🧬 Check if overlays are enabled via .env
def overlays_enabled():
    return os.getenv("ENABLE_ELEMENTAL_OVERLAYS", "false").lower() == "true"

# 🔱 Get elemental archetype for a given sector
def get_element_for_sector(sector, mappings):
    return mappings.get(sector, {"element": "Unknown", "symbol": "❓", "color": "#999999"})

# 🌀 Generate symbolic commentary (expandable)
def generate_commentary(sector, indicator_data, mappings):
    element_info = get_element_for_sector(sector, mappings)
    commentary = f"{element_info['symbol']} {sector} resonates with {element_info['element']} energy."
    
    # Example: Add dynamic lore based on RSI
    rsi = indicator_data.get("RSI", None)
    if rsi:
        if rsi > 70:
            commentary += " The fire burns high—momentum may be peaking."
        elif rsi < 30:
            commentary += " The waters recede—potential for reversal."
    
    return commentary
