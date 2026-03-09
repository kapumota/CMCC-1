from __future__ import annotations

import os
from pathlib import Path

from config.settings import Settings
from rag.index import TfidfIndex


def _read_docs(docs_dir: Path) -> list[tuple[str, str]]:
    docs: list[tuple[str, str]] = []
    for p in sorted(docs_dir.glob("**/*")):
        if p.is_dir():
            continue
        if p.suffix.lower() not in {".md", ".txt"}:
            continue
        docs.append((p.name, p.read_text(encoding="utf-8")))
    return docs


def _chunk(text: str, max_chars: int = 700) -> list[str]:
    # chunk by paragraphs; then merge small ones.
    paras = [t.strip() for t in text.split("\n\n") if t.strip()]
    chunks: list[str] = []
    buf = ""
    for para in paras:
        if len(buf) + len(para) + 2 <= max_chars:
            buf = (buf + "\n\n" + para).strip()
        else:
            if buf:
                chunks.append(buf)
            buf = para
    if buf:
        chunks.append(buf)
    return chunks


def main() -> None:
    s = Settings()
    docs_dir = Path(s.docs_dir)
    idx_dir = Path(s.index_dir)

    if not docs_dir.exists():
        raise SystemExit(f"Docs dir no existe: {docs_dir}")

    docs = _read_docs(docs_dir)
    if not docs:
        raise SystemExit(f"No hay documentos .md/.txt en {docs_dir}")

    chunks: list[str] = []
    chunk_ids: list[str] = []
    for fname, text in docs:
        for j, ch in enumerate(_chunk(text)):
            chunk_ids.append(f"{fname}::chunk{j}")
            chunks.append(ch)

    index = TfidfIndex.build(chunks=chunks, chunk_ids=chunk_ids)
    index.save(idx_dir)
    print(f"Index OK: {idx_dir} (chunks={len(chunks)})")


if __name__ == "__main__":
    main()
