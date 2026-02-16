import pandas as pd
import numpy as np


# ---------------------------------------------------------
# BUILD POSITION-BASED CTR BASELINE (PRE-CUTOFF)
# ---------------------------------------------------------

def build_position_ctr_baseline(df: pd.DataFrame, cutoff_date: str) -> pd.DataFrame:

    df_copy = df.copy()

    df_copy["date"] = pd.to_datetime(df_copy["date"])
    cutoff = pd.to_datetime(cutoff_date)

    # Filter pre-AI period
    before_df = df_copy[df_copy["date"] < cutoff].copy()

    if before_df.empty:
        return pd.DataFrame(columns=["position_bucket", "expected_ctr"])

    # Ensure numeric position
    before_df["position"] = pd.to_numeric(before_df["position"], errors="coerce")

    # Remove invalid rows
    before_df = before_df.dropna(subset=["position", "ctr"])

    # Position bucketing (floor to nearest integer)
    before_df["position_bucket"] = before_df["position"].apply(
        lambda x: int(np.floor(x)) if x >= 1 else 1
    )

    baseline = (
        before_df
        .groupby("position_bucket")["ctr"]
        .mean()
        .reset_index()
        .rename(columns={"ctr": "expected_ctr"})
    )

    return baseline


# ---------------------------------------------------------
# APPLY BASELINE MODEL TO POST-CUTOFF DATA
# ---------------------------------------------------------

def apply_baseline_model(
    df: pd.DataFrame,
    baseline: pd.DataFrame,
    cutoff_date: str
) -> pd.DataFrame:

    df_copy = df.copy()

    df_copy["date"] = pd.to_datetime(df_copy["date"])
    cutoff = pd.to_datetime(cutoff_date)

    # Filter post-AI period
    after_df = df_copy[df_copy["date"] >= cutoff].copy()

    if after_df.empty:
        return pd.DataFrame()

    after_df["position"] = pd.to_numeric(after_df["position"], errors="coerce")
    after_df = after_df.dropna(subset=["position", "ctr"])

    after_df["position_bucket"] = after_df["position"].apply(
        lambda x: int(np.floor(x)) if x >= 1 else 1
    )

    # Merge expected CTR baseline
    merged = after_df.merge(
        baseline,
        on="position_bucket",
        how="left"
    )

    # If no baseline match, fallback to actual CTR (no suppression)
    merged["expected_ctr"] = merged["expected_ctr"].fillna(merged["ctr"])

    # Suppression = expected - actual
    merged["ctr_suppression"] = (
        merged["expected_ctr"] - merged["ctr"]
    )

    # Prevent negative suppression (optional — PoC safe guard)
    merged["ctr_suppression"] = merged["ctr_suppression"].apply(
        lambda x: x if x > 0 else 0
    )

    return merged
