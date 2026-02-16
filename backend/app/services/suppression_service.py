import pandas as pd
import numpy as np

def compute_ctr_suppression(df, cutoff_date):

    df["date"] = pd.to_datetime(df["date"])
    cutoff_date = pd.to_datetime(cutoff_date)

    df["period"] = np.where(df["date"] < cutoff_date, "before", "after")

    grouped = df.groupby(["query", "period"]).agg({
        "ctr": "mean",
        "impressions": "mean",
        "position": "mean"
    }).reset_index()

    pivot = grouped.pivot(index="query", columns="period")

    pivot.columns = [
        f"{col[0]}_{col[1]}" for col in pivot.columns
    ]

    pivot = pivot.reset_index()

    pivot["ctr_loss"] = pivot["ctr_before"] - pivot["ctr_after"]
    pivot["position_change"] = abs(
        pivot["position_before"] - pivot["position_after"]
    )

    return pivot
