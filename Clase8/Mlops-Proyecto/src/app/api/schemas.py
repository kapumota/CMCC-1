from __future__ import annotations

from pydantic import BaseModel, Field


class WorkflowRequest(BaseModel):
    request: str = Field(..., min_length=3)
    top_k: int | None = Field(default=None, ge=1, le=10)
