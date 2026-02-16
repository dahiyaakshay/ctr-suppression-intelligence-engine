import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts"

export default function CTRChart({ data }: any) {
  return (
    <div style={{ height: 300 }}>
      <h3 style={{ color: "#FF6B35" }}>CTR Before vs After</h3>
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data}>
          <XAxis dataKey="query" hide />
          <YAxis />
          <Tooltip />
          <Line dataKey="ctr_before" stroke="#FF6B35" />
          <Line dataKey="ctr_after" stroke="#8884d8" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}
