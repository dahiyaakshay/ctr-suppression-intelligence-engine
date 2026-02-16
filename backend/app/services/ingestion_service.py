import pandas as pd
from app.utils.date_utils import ensure_datetime

REQUIRED_COLUMNS = [
    "query",
    "date",
    "ctr",
    "impressions",
    "position"
]

def validate_search_console(df: pd.DataFrame):

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return True


def load_search_console(path: str):

    df = pd.read_csv(path)
    validate_search_console(df)
    df = ensure_datetime(df, "date")

    return df
