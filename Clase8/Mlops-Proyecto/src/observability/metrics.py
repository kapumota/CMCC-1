from __future__ import annotations

from prometheus_client import Counter, Histogram


REQUESTS_TOTAL = Counter(
    "sesion8_requests_total",
    "Total de requests por endpoint",
    labelnames=("route", "status"),
)

WORKFLOW_LATENCY_MS = Histogram(
    "sesion8_workflow_latency_ms",
    "Latencia del workflow en milisegundos",
    buckets=(5, 10, 25, 50, 100, 250, 500, 1000, 2000, 5000),
)

TOOL_CALLS_TOTAL = Counter(
    "sesion8_tool_calls_total",
    "Total de tool calls",
    labelnames=("tool", "status"),
)

RAG_QUERIES_TOTAL = Counter(
    "sesion8_rag_queries_total",
    "Total de queries a RAG",
    labelnames=("status",),
)
