from pydantic import BaseModel
from typing import List

class AnalysisQuery(BaseModel):
    query: str
    ctr_before: float
    ctr_after: float
    ctr_loss: float
    estimated_revenue_loss: float
    p_value: float
    significant: bool
    risk_score: float
    risk_level: str


class AnalysisSummary(BaseModel):
    total_revenue_at_risk: float
    queries_analyzed: int
    significant_suppression_rate: float
