import { useEffect, useState } from "react"
import { getSummary, getFullAnalysis } from "../api/apiClient"

export function useAnalysis() {

  const [summary, setSummary] = useState<any>(null)
  const [queries, setQueries] = useState<any[]>([])
  const [projection, setProjection] = useState<any[]>([])
  const [intentSummary, setIntentSummary] = useState<any[]>([])
  const [monthly, setMonthly] = useState<any[]>([])

  useEffect(() => {

    async function load() {
      try {
        const summaryRes = await getSummary()
        const analysisRes = await getFullAnalysis()

        setSummary(summaryRes.data)

        setQueries(analysisRes.data?.queries || [])
        setProjection(analysisRes.data?.projection || [])
        setIntentSummary(analysisRes.data?.intent_summary || [])
        setMonthly(analysisRes.data?.monthly_suppression || [])

      } catch (err) {
        console.error("Failed to load analysis:", err)
      }
    }

    load()

  }, [])

  return {
    summary,
    queries,
    projection,
    intentSummary,
    monthly
  }
}
