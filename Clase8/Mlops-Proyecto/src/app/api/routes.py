from __future__ import annotations

import time
import uuid
import logging

from fastapi import APIRouter, Header, HTTPException
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from starlette.responses import Response

from config.settings import Settings
from observability.metrics import REQUESTS_TOTAL, WORKFLOW_LATENCY_MS
from rag.ingest import main as ingest_main
from rag.retriever import Retriever
from workflows.llm_client import LLMClient
from workflows.pipeline import run_workflow
from app.api.schemas import WorkflowRequest


router = APIRouter()
log = logging.getLogger("sesion8")

settings = Settings()
retriever = Retriever(settings=settings)
llm = LLMClient(settings=settings)

# Try load index at startup (safe if missing)
try:
    retriever.load()
except Exception:
    pass


@router.get("/health")
def health():
    return {
        "status": "ok",
        "env": settings.app_env,
        "rag_ready": retriever.is_ready(),
        "llm_enabled": llm.enabled(),
    }


@router.post("/workflow")
async def workflow(body: WorkflowRequest):
    request_id = uuid.uuid4().hex[:12]
    t0 = time.time()
    try:
        if not retriever.is_ready():
            # RAG is optional; still run workflow
            pass

        result = await run_workflow(settings=settings, retriever=retriever, llm=llm, user_text=body.request)
        status = "200"
        return result
    except Exception as e:
        status = "500"
        raise
    finally:
        latency_ms = (time.time() - t0) * 1000.0
        WORKFLOW_LATENCY_MS.observe(latency_ms)
        REQUESTS_TOTAL.labels(route="/workflow", status=status).inc()
        log.info("workflow_done", extra={"request_id": request_id, "route": "/workflow", "latency_ms": round(latency_ms, 2)})


@router.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)


@router.post("/admin/reindex")
def admin_reindex(x_admin_token: str | None = Header(default=None)):
    if x_admin_token != settings.admin_token:
        REQUESTS_TOTAL.labels(route="/admin/reindex", status="403").inc()
        raise HTTPException(status_code=403, detail="Forbidden")

    t0 = time.time()
    ingest_main()
    retriever.load()
    latency_ms = (time.time() - t0) * 1000.0
    REQUESTS_TOTAL.labels(route="/admin/reindex", status="200").inc()
    return {"status": "ok", "latency_ms": round(latency_ms, 2), "rag_ready": retriever.is_ready()}
