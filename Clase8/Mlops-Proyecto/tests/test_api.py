from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app


def test_health():
    c = TestClient(app)
    r = c.get("/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"


def test_workflow_runs():
    c = TestClient(app)
    r = c.post("/workflow", json={"request": "Viaje LAX JFK hotel New York 2 opciones"})
    assert r.status_code == 200
    data = r.json()
    assert "summary" in data
