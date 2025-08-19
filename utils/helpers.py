import html

def safe_ticker(ticker):
    return html.escape(ticker)

def map_sector_to_element(sector):
    from config.symbols import ELEMENTAL_MAP
    return ELEMENTAL_MAP.get(sector, "🌐")
