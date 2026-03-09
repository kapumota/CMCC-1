from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from observability.metrics import TOOL_CALLS_TOTAL
from tools.providers.provider_bootstrap import travel_provider, supported_locations


@dataclass
class ParsedRequest:
    departure_airport: str | None
    destination_airport: str | None
    hotel_city: str | None
    num_options: int


def parse_request(text: str) -> ParsedRequest:
    # Airports: tokens like LAX, JFK, etc.
    airports = re.findall(r"\b[A-Z]{3}\b", text)
    dep = airports[0] if len(airports) >= 1 else None
    dst = airports[1] if len(airports) >= 2 else None

    # Hotel city: heuristic over known cities (Sesión 8: luego se reemplaza por extracción con LLM)
    hotel_city = None
    for c in supported_locations.get("hotel_cities", []):
        if c.lower() in text.lower():
            hotel_city = c
            break

    m = re.search(r"(\d+)\s*opciones", text.lower())
    n = int(m.group(1)) if m else 3
    n = max(1, min(n, 5))

    return ParsedRequest(departure_airport=dep, destination_airport=dst, hotel_city=hotel_city, num_options=n)


def flight_lookup(dep: str, dst: str, n: int) -> dict[str, Any]:
    out = travel_provider.flight_lookup(dep, dst, num_options=n)
    if isinstance(out, dict) and "error" in out:
        TOOL_CALLS_TOTAL.labels(tool="flight_lookup", status="error").inc()
    else:
        TOOL_CALLS_TOTAL.labels(tool="flight_lookup", status="ok").inc()
    return out


def hotel_lookup(city: str, n: int) -> Any:
    out = travel_provider.hotel_lookup(city, num_options=n)
    if isinstance(out, dict) and "error" in out:
        TOOL_CALLS_TOTAL.labels(tool="hotel_lookup", status="error").inc()
    else:
        TOOL_CALLS_TOTAL.labels(tool="hotel_lookup", status="ok").inc()
    return out
