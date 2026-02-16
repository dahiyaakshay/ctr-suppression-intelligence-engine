import re
import pandas as pd

INFORMATIONAL_PATTERNS = [
    r"\bwhat\b",
    r"\bhow\b",
    r"\bwhy\b",
    r"\bguide\b",
    r"\bdefinition\b",
    r"\bexamples\b",
]

COMMERCIAL_PATTERNS = [
    r"\bbest\b",
    r"\breview\b",
    r"\btop\b",
    r"\bcompare\b",
    r"\bvs\b",
]

TRANSACTIONAL_PATTERNS = [
    r"\bbuy\b",
    r"\bprice\b",
    r"\bdiscount\b",
    r"\border\b",
]

def classify_intent(query: str):

    q = query.lower()

    for pattern in TRANSACTIONAL_PATTERNS:
        if re.search(pattern, q):
            return "Transactional"

    for pattern in COMMERCIAL_PATTERNS:
        if re.search(pattern, q):
            return "Commercial"

    for pattern in INFORMATIONAL_PATTERNS:
        if re.search(pattern, q):
            return "Informational"

    return "Navigational"


def apply_intent_classification(df: pd.DataFrame):

    df["intent"] = df["query"].apply(classify_intent)

    return df


def intent_impact_summary(df: pd.DataFrame):

    summary = (
        df.groupby("intent")
        .agg({
            "ctr_loss": "mean",
            "estimated_revenue_loss": "sum",
            "query": "count"
        })
        .reset_index()
        .rename(columns={"query": "query_count"})
    )

    return summary
