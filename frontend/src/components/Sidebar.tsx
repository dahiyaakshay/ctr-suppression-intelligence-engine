import { COLORS } from "../theme/colors"

export default function Sidebar() {
  return (
    <div
      style={{
        width: 240,
        background: "#14141A",
        padding: 30,
        borderRight: "1px solid rgba(255,255,255,0.05)",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between"
      }}
    >
      <div>
        <h2 style={{ color: COLORS.accent }}>CSI Engine</h2>

<div style={{ marginTop: 40 }}>
  <p style={{ marginBottom: 16, color: "#C5C7CE" }}>Dashboard</p>
  <p style={{ marginBottom: 16, color: "#9CA3AF" }}>Suppression</p>
  <p style={{ marginBottom: 16, color: "#9CA3AF" }}>Risk</p>
  <p style={{ marginBottom: 16, color: "#9CA3AF" }}>Projection</p>
</div>
      </div>

      <div style={{ fontSize: 12, color: COLORS.muted }}>
        v0.1 Intelligence Build
      </div>
    </div>
  )
}
