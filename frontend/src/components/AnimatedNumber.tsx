import { useEffect, useState } from "react"

export default function AnimatedNumber({ value }: any) {
  const [display, setDisplay] = useState(0)

  useEffect(() => {
    let start = 0
    const duration = 800
    const step = value / (duration / 16)

    const interval = setInterval(() => {
      start += step
      if (start >= value) {
        start = value
        clearInterval(interval)
      }
      setDisplay(Number(start.toFixed(2)))
    }, 16)

    return () => clearInterval(interval)
  }, [value])

  return <>{display}</>
}
