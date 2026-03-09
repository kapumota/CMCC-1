from __future__ import annotations

import time
from typing import Any

from config.settings import Settings
from rag.retriever import Retriever
from workflows.llm_client import LLMClient
from workflows.nodes import parse_request
from tools.providers.provider_bootstrap import travel_provider, supported_locations
from workflows.nodes import flight_lookup, hotel_lookup


SYSTEM_PROMPT = """Eres un asistente que sintetiza un plan de viaje.
Usa el contexto RAG si es relevante y resume en bullets. Evita información inventada."""


async def run_workflow(settings: Settings, retriever: Retriever, llm: LLMClient, user_text: str) -> dict[str, Any]:
    parsed = parse_request(user_text)

    # Ensure airports/cities are from our supported lists
    dep = parsed.departure_airport
    dst = parsed.destination_airport
    city = parsed.hotel_city

    rag_ctx = retriever.query(user_text, top_k=settings.top_k)

    flights = None
    hotels = None
    errors: list[str] = []

    if dep and dst:
        flights = flight_lookup(dep, dst, parsed.num_options)
        if isinstance(flights, dict) and flights.get("error"):
            errors.append(flights["error"])
    else:
        errors.append("No pude identificar aeropuerto de salida/destino (usa códigos como LAX, JFK).")

    if city:
        hotels = hotel_lookup(city, parsed.num_options)
        if isinstance(hotels, dict) and hotels.get("error"):
            errors.append(hotels["error"])
    else:
        errors.append("No pude identificar ciudad de hotel (ej: New York, Seattle).")

    # Compose a summary via LLM (optional) or fallback
    user_for_llm = (
        f"Solicitud: {user_text}\n\n"
        f"Contexto RAG (top {settings.top_k}):\n" +
        "\n---\n".join([c["text"] for c in rag_ctx]) + "\n\n"
        f"Vuelos: {flights}\n\n"
        f"Hoteles: {hotels}\n\n"
        f"Errores: {errors}\n"
    )
    summary = await llm.summarize(system=SYSTEM_PROMPT, user=user_for_llm)

    return {
        "parsed": parsed.__dict__,
        "rag": rag_ctx,
        "flights": flights,
        "hotels": hotels,
        "errors": errors,
        "summary": summary,
        "supported": supported_locations,
    }
