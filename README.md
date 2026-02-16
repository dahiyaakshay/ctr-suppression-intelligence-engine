# CTR Suppression Intelligence Engine

Baseline-adjusted CTR suppression modeling engine designed to measure AI search impact on organic revenue using statistical validation, volatility scoring, and revenue projection.

---

## Overview

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue)
![Status](https://img.shields.io/badge/Status-PoC-orange)

The CTR Suppression Intelligence Engine is a full-stack analytics system built to quantify organic traffic loss caused by interface-driven suppression (e.g., AI Overviews, zero-click search behavior).

This engine moves beyond simple before/after comparisons by implementing:

- Position-normalized CTR baselines
- Statistical significance testing
- Volatility modeling
- Intent-level suppression analysis
- Revenue impact estimation
- 6-month revenue projection modeling

---

## Problem Statement

AI-driven search interfaces (AI Overviews, zero-click answers, enriched SERPs) suppress organic click-through rates even when rankings remain stable.

Traditional SEO tools cannot isolate:

- Interface-driven suppression
- Revenue loss from zero-click behavior
- Volatility patterns post-AI rollout
- Query-level vulnerability

This engine solves that by modeling expected CTR behavior and measuring deviation statistically.

---

## Architecture

**Frontend:** React + TypeScript + Recharts  
**Backend:** FastAPI + Pandas + NumPy + SciPy  
**Data Source:** Google Search Console export (CSV)

```
Frontend Dashboard
        ↓
FastAPI API Layer
        ↓
Suppression Engine
        ├── Statistical Engine
        ├── Baseline Model
        ├── Volatility Engine
        ├── Revenue Engine
        └── Risk Scoring Layer
```

---

## Core Capabilities

### 1. Baseline-Adjusted CTR Modeling
Builds expected CTR per ranking position and calculates suppression relative to historical behavior.

### 2. Ranking Stability Filtering
Removes queries with ranking shifts to isolate interface-level impact.

### 3. Statistical Validation
Uses two-sample t-tests to validate suppression significance.

### 4. Revenue Modeling
Estimates lost revenue using:
- Lost Clicks
- Conversion Rate
- Average Order Value

### 5. Volatility Scoring
Detects CTR instability using rolling suppression modeling.

### 6. Intent Classification
Classifies queries into:
- Informational
- Commercial
- Transactional
- Navigational

### 7. Risk Scoring
Combines:
- Effective CTR loss
- Revenue exposure
- Statistical significance
- Volatility factor

### 8. Executive Dashboard
Provides:
- KPI overview
- Suppression heatmap
- Intent impact analysis
- Revenue projection
- High-risk query detection

---

## Methodology

1. Build historical CTR baseline by ranking position
2. Apply baseline to post-cutoff data
3. Filter queries with ranking instability
4. Validate suppression via statistical testing
5. Model revenue loss using conversion assumptions
6. Calculate volatility-adjusted risk score
7. Project 6-month exposure

---

## Running the Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Access:**
```
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

```bash
cd frontend
npm install
npm run dev
```

**Access:**
```
http://localhost:5173
```

---

## Data Format Required

Search Console CSV format:

```csv
query,date,ctr,impressions,position
```

Cutoff date is configurable in:
```
backend/app/config.py
```

---

## Why This Matters

AI-generated search interfaces reduce click-through rates even when rankings remain stable.

This engine provides a quantifiable framework to measure:

- Interface-driven revenue suppression
- AI overview exposure risk
- Query-level vulnerability
- Strategic SEO exposure

---

## Status

**Proof of Concept (PoC)** — Fully functional end-to-end system.

**Future Enhancements:**
- SERP AI detection simulation
- Multi-tenant support
- Database persistence
- SaaS deployment layer
