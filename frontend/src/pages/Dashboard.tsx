import AppLayout from "../layout/AppLayout"
import { useAnalysis } from "../hooks/useAnalysis"
import ExecutiveSummary from "../components/ExecutiveSummary"
import CTRChart from "../components/CTRChart"
import HighRiskTable from "../components/HighRiskTable"
import ProjectionChart from "../components/ProjectionChart"
import RiskHeatmap from "../components/RiskHeatmap"
import IntentBreakdown from "../components/IntentBreakdown"
import SuppressionTrendChart from "../components/SuppressionTrendChart"
import SectionHeader from "../components/SectionHeader"
import Card from "../components/Card"

export default function Dashboard() {

  const {
    summary,
    queries,
    projection,
    intentSummary,
    monthly
  } = useAnalysis()

  if (!summary) return null

  return (
    <AppLayout>

      <SectionHeader title="Executive Overview" />
      <ExecutiveSummary summary={summary} />

      <SectionHeader title="Suppression Intelligence" />
      <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr", gap: 24 }}>
        <Card><CTRChart data={queries} /></Card>
        <Card><IntentBreakdown data={intentSummary} /></Card>
      </div>

      <SectionHeader title="Risk Analysis" />
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24 }}>
        <Card><RiskHeatmap data={queries} /></Card>
        <Card><SuppressionTrendChart data={monthly} /></Card>
      </div>

      <SectionHeader title="Revenue Exposure" />
      <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr", gap: 24 }}>
        <Card><HighRiskTable data={queries} /></Card>
        <Card><ProjectionChart data={projection} /></Card>
      </div>

    </AppLayout>
  )
}
