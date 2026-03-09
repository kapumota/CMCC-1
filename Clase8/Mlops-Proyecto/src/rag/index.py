from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

@dataclass
class TfidfIndex:
    vectorizer: TfidfVectorizer
    matrix: "np.ndarray"
    chunks: List[str]
    chunk_ids: List[str]

    @staticmethod
    def build(chunks: List[str], chunk_ids: List[str]) -> "TfidfIndex":
        vectorizer = TfidfVectorizer(stop_words=None, max_features=5000)
        matrix = vectorizer.fit_transform(chunks)
        return TfidfIndex(vectorizer=vectorizer, matrix=matrix, chunks=chunks, chunk_ids=chunk_ids)

    def save(self, out_dir: str | Path) -> None:
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.vectorizer, out / "tfidf_vectorizer.joblib")
        joblib.dump(self.matrix, out / "tfidf_matrix.joblib")
        joblib.dump(self.chunks, out / "chunks.joblib")
        joblib.dump(self.chunk_ids, out / "chunk_ids.joblib")

    @staticmethod
    def load(in_dir: str | Path) -> "TfidfIndex":
        inp = Path(in_dir)
        vectorizer = joblib.load(inp / "tfidf_vectorizer.joblib")
        matrix = joblib.load(inp / "tfidf_matrix.joblib")
        chunks = joblib.load(inp / "chunks.joblib")
        chunk_ids = joblib.load(inp / "chunk_ids.joblib")
        return TfidfIndex(vectorizer=vectorizer, matrix=matrix, chunks=chunks, chunk_ids=chunk_ids)

    def query(self, text: str, top_k: int = 3) -> List[Tuple[str, str, float]]:
        # retorna (chunk_id, chunk_text, score)
        q = self.vectorizer.transform([text])
        scores = (self.matrix @ q.T).toarray().ravel()
        if len(scores) == 0:
            return []
        idx = np.argsort(scores)[::-1][:top_k]
        results = []
        for i in idx:
            results.append((self.chunk_ids[int(i)], self.chunks[int(i)], float(scores[int(i)])))
        return results
