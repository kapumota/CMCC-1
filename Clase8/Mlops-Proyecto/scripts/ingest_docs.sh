#!/usr/bin/env bash
set -euo pipefail
export PYTHONPATH=./src
if [ -f .env ]; then
  set -a; source .env; set +a
fi
python -m rag.ingest
echo "OK: índice construido en ${INDEX_DIR:-./data/indexes}"
