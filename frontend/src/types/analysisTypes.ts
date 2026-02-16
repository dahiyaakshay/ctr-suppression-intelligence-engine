export interface QueryResult {
  query: string
  ctr_before: number
  ctr_after: number
  ctr_loss: number
  estimated_revenue_loss: number
  p_value: number
  significant: boolean
  risk_score: number
  risk_level: string
}

export interface Summary {
  total_revenue_at_risk: number
  queries_analyzed: number
  significant_suppression_rate: number
  average_ctr_loss: number
}

export interface Projection {
  month: string
  projected_revenue_loss: number
}
