from __future__ import annotations

import json
from pathlib import Path

def load_supported_locations() -> dict:
    here = Path(__file__).resolve().parent
    # Our project keeps JSON in src/resources/
    # travel_provider.py keeps its own supported_locations.json next to itself,
    # but we also ship a copy in src/resources for clarity.
    candidate = (here.parent.parent / "resources" / "supported_locations.json").resolve()
    if candidate.exists():
        return json.loads(candidate.read_text(encoding="utf-8"))
    # fallback: same dir as travel_provider
    candidate2 = (here / "supported_locations.json").resolve()
    if candidate2.exists():
        return json.loads(candidate2.read_text(encoding="utf-8"))
    return {"airports": [], "hotel_cities": []}
