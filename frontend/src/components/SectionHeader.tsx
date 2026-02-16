import { COLORS } from "../theme/colors"

export default function SectionHeader({ title }: any) {
  return (
    <div style={{ marginBottom: 20 }}>
      <h2 style={{ color: COLORS.accent, marginBottom: 6 }}>
        {title}
      </h2>
      <div
        style={{
          height: 3,
          width: 60,
          background: `linear-gradient(90deg, ${COLORS.accent}, transparent)`
        }}
      />
    </div>
  )
}
