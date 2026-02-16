import { COLORS } from "../theme/colors"

export default function Card({ children }: any) {
  return (
    <div
      className="card-hover"
      style={{
        background: "rgba(255,255,255,0.04)",
        backdropFilter: "blur(8px)",
        borderRadius: 20,
        padding: 28,
        border: "1px solid rgba(255,255,255,0.06)",
        transition: "all 0.2s ease"
      }}
    >
      {children}
    </div>
  )
}
