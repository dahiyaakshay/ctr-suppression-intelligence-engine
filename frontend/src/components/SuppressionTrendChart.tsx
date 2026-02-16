import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts"

import { COLORS } from "../theme/colors"

export default function SuppressionTrendChart({ data }: any) {

  if (!data || data.length === 0) return null

  return (
    <div style={{ height: 350, marginTop: 40 }}>
      <h3 style={{ color: COLORS.accent }}>
        CTR Suppression Trend
      </h3>

      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data}>
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line dataKey="ctr" stroke="#8884d8" />
          <Line dataKey="rolling_ctr" stroke={COLORS.accent} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}
