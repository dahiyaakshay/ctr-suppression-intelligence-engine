#!/bin/bash

echo "Starting CTR Suppression Intelligence Engine..."

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload