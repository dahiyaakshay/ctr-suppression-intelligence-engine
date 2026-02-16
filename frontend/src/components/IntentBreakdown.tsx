import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts"

import { COLORS } from "../theme/colors"

interface Props {
  data: any[]
}

export default function IntentBreakdown({ data }: Props) {

  if (!data || data.length === 0) return null

  return (
    <div style={{ height: 350, marginTop: 40 }}>

      <h3 style={{ color: COLORS.accent }}>
        Suppression Impact by Intent
      </h3>

      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data}>

          <CartesianGrid stroke="#333" />

          <XAxis dataKey="intent" stroke="#aaa" />
          <YAxis stroke="#aaa" />

          <Tooltip
            contentStyle={{
              backgroundColor: COLORS.card,
              border: "1px solid #333",
              color: "white"
            }}
          />

          <Bar
            dataKey="estimated_revenue_loss"
            fill={COLORS.accent}
          />

        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}
