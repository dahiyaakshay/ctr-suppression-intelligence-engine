import Sidebar from "../components/Sidebar"
import { COLORS } from "../theme/colors"

export default function AppLayout({ children }: any) {
  return (
    <div style={{ display: "flex", minHeight: "100vh" }}>
      <Sidebar />

      <div
        style={{
          flex: 1,
          background: COLORS.background,
          padding: "60px 60px 80px 60px"
        }}
      >
        {children}
      </div>
    </div>
  )
}
