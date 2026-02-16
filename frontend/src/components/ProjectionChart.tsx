import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts"

export default function ProjectionChart({ data }: any) {
  return (
    <div style={{ height: 300, marginTop: 30 }}>
      <h3 style={{ color: "#FF6B35" }}>6-Month Revenue Projection</h3>
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data}>
          <XAxis dataKey="month" />
          <YAxis />
          <Tooltip />
          <Line dataKey="projected_revenue_loss" stroke="#FF6B35" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}
