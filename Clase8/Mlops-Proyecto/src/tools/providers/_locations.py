from __future__ import annotations

import json
from pathlib import Path

def load_supported_locations() -> dict:
    here = Path(__file__).resolve().parent
    # El proyecto guarda JSON en src/resources/
    # travel_provider.py guarda su propio archivo support_locations.json junto a sí mismo,
    # pero también enviamos una copia en src/resources para mayor claridad.
    
    candidate = (here.parent.parent / "resources" / "supported_locations.json").resolve()
    if candidate.exists():
        return json.loads(candidate.read_text(encoding="utf-8"))
    # fallback: mismo dir como travel_provider
    candidate2 = (here / "supported_locations.json").resolve()
    if candidate2.exists():
        return json.loads(candidate2.read_text(encoding="utf-8"))
    return {"airports": [], "hotel_cities": []}
