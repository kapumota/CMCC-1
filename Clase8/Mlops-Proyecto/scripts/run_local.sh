#!/usr/bin/env bash
set -euo pipefail
export PYTHONPATH=./src
if [ -f .env ]; then
  set -a; source .env; set +a
fi
uvicorn app.main:app --host "${HOST:-127.0.0.1}" --port "${PORT:-8000}" --reload
