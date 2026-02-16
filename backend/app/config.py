import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

SEARCH_CONSOLE_PATH = os.path.join(DATA_DIR, "search_console.csv")
GA4_PATH = os.path.join(DATA_DIR, "ga4.csv")

CUTOFF_DATE = "2024-05-01"

POSITION_THRESHOLD = 0.5
DEFAULT_CONVERSION_RATE = 0.02
DEFAULT_AOV = 150
