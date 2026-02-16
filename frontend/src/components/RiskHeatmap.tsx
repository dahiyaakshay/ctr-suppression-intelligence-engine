import {
  ScatterChart,
  Scatter,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts"

import { COLORS } from "../theme/colors"

function CustomTooltip({ active, payload }: any) {
  if (active && payload && payload.length) {
    const data = payload[0].payload

    return (
      <div
        style={{
          background: "rgba(20, 20, 26, 0.95)",
          border: "1px solid rgba(255,255,255,0.1)",
          padding: 12,
          borderRadius: 12,
          color: "#FFFFFF",
          fontSize: 13
        }}
      >
        <div style={{ marginBottom: 6, fontWeight: 600 }}>
          {data.query}
        </div>

        <div>CTR Loss: {Number(data.effective_loss).toFixed(2)}</div>
        <div>Revenue Loss: ${Number(data.estimated_revenue_loss).toFixed(2)}</div>
        <div>Risk Score: {Number(data.risk_score).toFixed(2)}</div>
      </div>
    )
  }

  return null
}

export default function RiskHeatmap({ data }: any) {

  const formatted = data.map((d: any) => ({
    ...d,
    effective_loss: Number(d.effective_loss || 0),
    estimated_revenue_loss: Number(d.estimated_revenue_loss || 0),
    risk_score: Number(d.risk_score || 0)
  }))

  return (
    <div style={{ height: 320 }}>
      <ResponsiveContainer width="100%" height="100%">
        <ScatterChart>
          <XAxis
            dataKey="effective_loss"
            stroke="#9CA3AF"
            tickFormatter={(val) => Number(val).toFixed(2)}
          />
          <YAxis
            dataKey="estimated_revenue_loss"
            stroke="#9CA3AF"
            tickFormatter={(val) => Number(val).toFixed(2)}
          />

          <Tooltip content={<CustomTooltip />} />

          <Scatter
            data={formatted}
            fill={COLORS.accent}
          />
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  )
}
