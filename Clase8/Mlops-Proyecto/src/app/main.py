from __future__ import annotations

import logging
from fastapi import FastAPI

from observability.logging import setup_logging
from app.api.routes import router


setup_logging(level=logging.INFO)

app = FastAPI(title="Sesión 8 – Workflows/Pipelines LLM (Mini‑proyecto)")
app.include_router(router)
