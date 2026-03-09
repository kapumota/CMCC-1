from __future__ import annotations

from pathlib import Path

from config.settings import Settings
from observability.metrics import RAG_QUERIES_TOTAL
from rag.index import TfidfIndex


class Retriever:
    def __init__(self, settings: Settings):
        self.settings = settings
        self._index: TfidfIndex | None = None

    def load(self) -> None:
        self._index = TfidfIndex.load(self.settings.index_dir)

    def is_ready(self) -> bool:
        return self._index is not None

    def query(self, text: str, top_k: int | None = None) -> list[dict]:
        if self._index is None:
            RAG_QUERIES_TOTAL.labels(status="not_ready").inc()
            return []
        RAG_QUERIES_TOTAL.labels(status="ok").inc()
        k = top_k or self.settings.top_k
        results = self._index.query(text, top_k=k)
        return [
            {"chunk_id": cid, "text": ch, "score": score}
            for (cid, ch, score) in results
        ]
