import pandas as pd

def build_monthly_suppression(df, cutoff_date):

    df["date"] = pd.to_datetime(df["date"])
    cutoff_date = pd.to_datetime(cutoff_date)

    df["period"] = df["date"].apply(
        lambda x: "before" if x < cutoff_date else "after"
    )

    monthly = (
        df.groupby(["date"])
        .agg({
            "ctr": "mean"
        })
        .reset_index()
        .sort_values("date")
    )

    monthly["rolling_ctr"] = monthly["ctr"].rolling(3).mean()

    monthly["volatility"] = (
        monthly["rolling_ctr"].diff().abs()
    )

    return monthly


def compute_volatility_score(monthly_df):

    if len(monthly_df) == 0:
        return 0

    return monthly_df["volatility"].mean()
