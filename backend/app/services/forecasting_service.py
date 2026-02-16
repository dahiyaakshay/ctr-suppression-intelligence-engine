import pandas as pd

def project_6_month_loss(df):

    # Simple linear projection using average monthly loss
    avg_monthly_loss = df["estimated_revenue_loss"].mean()

    projection = []

    for month in range(1, 7):
        projection.append({
            "month": f"Month {month}",
            "projected_revenue_loss": round(avg_monthly_loss * month, 2)
        })

    return projection
