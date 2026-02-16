from fastapi import APIRouter
import pandas as pd
import numpy as np

from app.config import (
    SEARCH_CONSOLE_PATH,
    CUTOFF_DATE,
    POSITION_THRESHOLD,
    DEFAULT_CONVERSION_RATE,
    DEFAULT_AOV
)

from app.services.ingestion_service import load_search_console
from app.services.suppression_service import compute_ctr_suppression
from app.services.statistics_service import compute_significance
from app.services.revenue_service import estimate_revenue_loss
from app.services.baseline_model_service import (
    build_position_ctr_baseline,
    apply_baseline_model
)
from app.services.forecasting_service import project_6_month_loss
from app.services.intent_service import (
    apply_intent_classification,
    intent_impact_summary
)
from app.services.timeseries_service import (
    build_monthly_suppression,
    compute_volatility_score
)
from app.services.risk_service import compute_risk_score

router = APIRouter(prefix="/analysis")


# ---------------------------------------------------------
# CORE PIPELINE
# ---------------------------------------------------------

def run_full_pipeline():

    df = load_search_console(SEARCH_CONSOLE_PATH)

    # ---------------------------
    # BASELINE MODEL
    # ---------------------------

    baseline = build_position_ctr_baseline(df, CUTOFF_DATE)
    baseline_applied = apply_baseline_model(df, baseline, CUTOFF_DATE)

    if not baseline_applied.empty:
        baseline_query = (
            baseline_applied
            .groupby("query")["ctr_suppression"]
            .mean()
            .reset_index()
        )
    else:
        baseline_query = pd.DataFrame(columns=["query", "ctr_suppression"])

    # ---------------------------
    # SUPPRESSION MODEL
    # ---------------------------

    suppression_df = compute_ctr_suppression(df, CUTOFF_DATE)

    suppression_df = suppression_df[
        suppression_df["position_change"] <= POSITION_THRESHOLD
    ]

    significance_df = compute_significance(df, CUTOFF_DATE)

    merged = suppression_df.merge(significance_df, on="query", how="left")
    merged = merged.merge(baseline_query, on="query", how="left")

    merged = estimate_revenue_loss(
        merged,
        DEFAULT_CONVERSION_RATE,
        DEFAULT_AOV
    )

    # ---------------------------
    # TIME-SERIES + VOLATILITY
    # ---------------------------

    monthly = build_monthly_suppression(df, CUTOFF_DATE)
    volatility_score = compute_volatility_score(monthly)

    # ---------------------------
    # RISK SCORING
    # ---------------------------

    final_df = compute_risk_score(merged, volatility_score)

    # ---------------------------
    # INTENT CLASSIFICATION
    # ---------------------------

    final_df = apply_intent_classification(final_df)
    intent_summary = intent_impact_summary(final_df)

    # ---------------------------
    # PROJECTION
    # ---------------------------

    projection = project_6_month_loss(final_df)

    # ---------------------------
    # SANITIZE DATA FOR JSON
    # ---------------------------

    def clean_dataframe(df_to_clean):
        if df_to_clean is None or len(df_to_clean) == 0:
            return df_to_clean

        df_to_clean = df_to_clean.replace(
            [np.inf, -np.inf],
            0
        ).fillna(0)

        return df_to_clean

    final_df = clean_dataframe(final_df)
    baseline_applied = clean_dataframe(baseline_applied)
    monthly = clean_dataframe(monthly)
    intent_summary = clean_dataframe(intent_summary)

    return final_df, baseline_applied, projection, intent_summary, monthly


# ---------------------------------------------------------
# ENDPOINTS
# ---------------------------------------------------------

@router.get("/run")
def run_analysis():

    final_df, baseline_applied, projection, intent_summary, monthly = run_full_pipeline()

    return {
        "queries": final_df.to_dict(orient="records"),
        "baseline_suppression": (
            baseline_applied.to_dict(orient="records")
            if baseline_applied is not None else []
        ),
        "projection": projection,
        "intent_summary": (
            intent_summary.to_dict(orient="records")
            if intent_summary is not None else []
        ),
        "monthly_suppression": (
            monthly.to_dict(orient="records")
            if monthly is not None else []
        )
    }


@router.get("/summary")
def get_summary():

    final_df, _, _, _, _ = run_full_pipeline()

    if final_df is None or len(final_df) == 0:
        return {
            "total_revenue_at_risk": 0,
            "queries_analyzed": 0,
            "significant_suppression_rate": 0,
            "average_ctr_loss": 0
        }

    total_revenue = final_df["estimated_revenue_loss"].sum()
    total_queries = len(final_df)

    significant_rate = (
        final_df["significant"].sum() / total_queries
        if total_queries > 0 else 0
    )

    avg_ctr_loss = (
        final_df["effective_loss"].mean()
        if total_queries > 0 else 0
    )

    return {
        "total_revenue_at_risk": round(float(total_revenue), 2),
        "queries_analyzed": int(total_queries),
        "significant_suppression_rate": round(float(significant_rate), 3),
        "average_ctr_loss": round(float(avg_ctr_loss), 4)
    }


@router.get("/high-risk")
def get_high_risk():

    final_df, _, _, _, _ = run_full_pipeline()

    if final_df is None or len(final_df) == 0:
        return []

    high_risk = final_df[
        final_df["risk_level"].isin(["High", "Critical"])
    ]

    return high_risk.to_dict(orient="records")


@router.get("/projection")
def get_projection():

    _, _, projection, _, _ = run_full_pipeline()

    return projection if projection else []
