import pandas as pd

def ensure_datetime(df, column="date"):
    df[column] = pd.to_datetime(df[column])
    return df


def label_period(df, cutoff_date, column="date"):
    cutoff_date = pd.to_datetime(cutoff_date)
    df["period"] = df[column].apply(
        lambda x: "before" if x < cutoff_date else "after"
    )
    return df
