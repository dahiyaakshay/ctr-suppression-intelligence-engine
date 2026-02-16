import Card from "./Card"
import AnimatedNumber from "./AnimatedNumber"
import { COLORS } from "../theme/colors"

export default function ExecutiveSummary({ summary }: any) {
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))",
        gap: 24,
        marginBottom: 50
      }}
    >
      <Card>
        <p style={{ color: COLORS.muted }}>Revenue at Risk</p>
        <h1 style={{ color: COLORS.accent }}>
          $<AnimatedNumber value={summary.total_revenue_at_risk} />
        </h1>
      </Card>

      <Card>
        <p style={{ color: COLORS.muted }}>Queries Analyzed</p>
        <h1><AnimatedNumber value={summary.queries_analyzed} /></h1>
      </Card>

      <Card>
        <p style={{ color: COLORS.muted }}>Significant Suppression</p>
        <h1>
          <AnimatedNumber value={summary.significant_suppression_rate * 100} />%
        </h1>
      </Card>

      <Card>
        <p style={{ color: COLORS.muted }}>Avg CTR Loss</p>
        <h1><AnimatedNumber value={summary.average_ctr_loss} /></h1>
      </Card>
    </div>
  )
}
