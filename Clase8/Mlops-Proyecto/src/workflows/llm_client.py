from __future__ import annotations

import os
from typing import Any

import httpx

from config.settings import Settings


class LLMClient:
    """Cliente para un endpoint OpenAI-compatible /v1/chat/completions (opcional)."""

    def __init__(self, settings: Settings):
        self.s = settings

    def enabled(self) -> bool:
        return bool(self.s.llm_base_url and self.s.llm_api_key is not None)

    async def summarize(self, system: str, user: str) -> str:
        # Fallback local si no hay LLM
        if not self.enabled():
            return self._fallback(system=system, user=user)

        url = self.s.llm_base_url.rstrip("/") + "/chat/completions"
        headers = {"Authorization": f"Bearer {self.s.llm_api_key}"}
        payload: dict[str, Any] = {
            "model": self.s.llm_model,
            "temperature": self.s.llm_temperature,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }

        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.post(url, json=payload, headers=headers)
            r.raise_for_status()
            data = r.json()
            return data["choices"][0]["message"]["content"]

    def _fallback(self, system: str, user: str) -> str:
        # Respuesta deterministic/plantilla para correr offline
        # (Sesión 8: el foco es pipeline + ops, no "calidad de lenguaje")
        return (
            "Resumen (fallback local):\n"
            f"- Objetivo: {user[:140]}{'...' if len(user)>140 else ''}\n"
            "- Nota: configura LLM_BASE_URL/LLM_API_KEY para usar un LLM real."
        )
