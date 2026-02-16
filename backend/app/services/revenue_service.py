def estimate_revenue_loss(df, conversion_rate, avg_order_value):

    df["lost_clicks"] = df["impressions_after"] * df["ctr_loss"]

    df["estimated_revenue_loss"] = (
        df["lost_clicks"] *
        conversion_rate *
        avg_order_value
    )

    return df
