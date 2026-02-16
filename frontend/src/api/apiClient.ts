import axios from "axios"

const API = axios.create({
  baseURL: "http://127.0.0.1:8000"
})

export const getSummary = () => API.get("/analysis/summary")
export const getFullAnalysis = () => API.get("/analysis/run")
export const getProjection = () => API.get("/analysis/projection")
