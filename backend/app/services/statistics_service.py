import pandas as pd
from scipy.stats import ttest_ind

def compute_significance(df, cutoff_date):

    df["date"] = pd.to_datetime(df["date"])
    cutoff_date = pd.to_datetime(cutoff_date)

    results = []

    for query in df["query"].unique():

        q_data = df[df["query"] == query]

        before = q_data[q_data["date"] < cutoff_date]["ctr"]
        after = q_data[q_data["date"] >= cutoff_date]["ctr"]

        if len(before) > 1 and len(after) > 1:
            stat, p_value = ttest_ind(before, after, equal_var=False)
        else:
            p_value = 1.0

        results.append({
            "query": query,
            "p_value": float(p_value),
            "significant": p_value < 0.05
        })

    return pd.DataFrame(results)
