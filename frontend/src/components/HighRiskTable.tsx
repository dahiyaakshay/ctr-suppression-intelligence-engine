import { COLORS } from "../theme/colors"

export default function HighRiskTable({ data }: any) {

  const highRisk = data.filter(
    (q: any) => q.risk_level === "High" || q.risk_level === "Critical"
  )

  return (
    <div>

      <h2 style={{ marginBottom: 24 }}>
        High Risk Queries
      </h2>

      {/* Header Row */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "2fr 1fr 1fr 1fr",
          padding: "12px 0",
          borderBottom: "1px solid rgba(255,255,255,0.08)",
          color: COLORS.muted,
          fontSize: 13,
          fontWeight: 500
        }}
      >
        <div>Query</div>
        <div>CTR Loss</div>
        <div>Revenue Loss</div>
        <div>Risk</div>
      </div>

      {/* Data Rows */}
      {highRisk.map((row: any, index: number) => (
        <div
          key={index}
          style={{
            display: "grid",
            gridTemplateColumns: "2fr 1fr 1fr 1fr",
            padding: "14px 0",
            borderBottom: "1px solid rgba(255,255,255,0.04)",
            fontSize: 14
          }}
          className="row-hover"
        >
          <div style={{ color: "#FFFFFF" }}>
            {row.query}
          </div>

          <div>
            {Number(row.effective_loss).toFixed(3)}
          </div>

          <div>
            ${Number(row.estimated_revenue_loss).toFixed(2)}
          </div>

          <div
            style={{
              color:
                row.risk_level === "Critical"
                  ? "#FF4D4D"
                  : COLORS.accent,
              fontWeight: 600
            }}
          >
            {row.risk_level}
          </div>
        </div>
      ))}

      {highRisk.length === 0 && (
        <div style={{ padding: 20, color: COLORS.muted }}>
          No high-risk queries detected.
        </div>
      )}

    </div>
  )
}
