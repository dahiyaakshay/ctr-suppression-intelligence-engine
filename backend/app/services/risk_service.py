def compute_risk_score(df, volatility_score=0):

    # Baseline-adjusted suppression
    if "ctr_suppression" in df.columns:
        df["effective_loss"] = df["ctr_suppression"].fillna(df["ctr_loss"])
    else:
        df["effective_loss"] = df["ctr_loss"]

    max_loss = df["effective_loss"].max()
    max_revenue = df["estimated_revenue_loss"].max()

    df["normalized_loss"] = (
        df["effective_loss"] / max_loss
        if max_loss != 0 else 0
    )

    df["normalized_revenue"] = (
        df["estimated_revenue_loss"] / max_revenue
        if max_revenue != 0 else 0
    )

    # Normalize volatility
    normalized_volatility = min(volatility_score * 10, 1)

    df["risk_score"] = (
        df["normalized_loss"] * 0.35 +
        df["normalized_revenue"] * 0.35 +
        df["significant"].astype(int) * 0.2 +
        normalized_volatility * 0.1
    )

    def label(score):
        if score > 0.75:
            return "Critical"
        elif score > 0.5:
            return "High"
        elif score > 0.25:
            return "Moderate"
        return "Low"

    df["risk_level"] = df["risk_score"].apply(label)

    return df
