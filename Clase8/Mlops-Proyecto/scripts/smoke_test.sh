#!/usr/bin/env bash
set -euo pipefail
python - <<'PY'
import requests, json, time
base="http://127.0.0.1:8000"
print("health:", requests.get(base+"/health", timeout=5).json())
payload={"request":"Quiero viajar de LAX a JFK y hospedarme en New York. Dame 2 opciones."}
r=requests.post(base+"/workflow", json=payload, timeout=10)
print("workflow status:", r.status_code)
print(json.dumps(r.json(), indent=2, ensure_ascii=False))
PY
