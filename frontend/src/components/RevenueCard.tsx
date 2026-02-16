import { COLORS } from "../theme/colors"

interface Props {
  title: string
  value: number
  subtitle?: string
}

export default function RevenueCard({ title, value, subtitle }: Props) {
  return (
    <div
      style={{
        background: COLORS.card,
        padding: "20px",
        borderRadius: "12px",
        marginBottom: "20px",
        boxShadow: "0 0 0 1px rgba(255,255,255,0.05)"
      }}
    >
      <h4 style={{ color: COLORS.muted, marginBottom: 10 }}>
        {title}
      </h4>

      <h2 style={{ color: COLORS.accent, margin: 0 }}>
        ${value.toLocaleString()}
      </h2>

      {subtitle && (
        <p style={{ color: COLORS.muted, marginTop: 8 }}>
          {subtitle}
        </p>
      )}
    </div>
  )
}
