from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_task():
    res = client.post("/tasks/", json={"title": "Test Task"})
    assert res.status_code == 200
    assert res.json()["title"] == "Test Task"


def test_read_tasks():
    res = client.get("/tasks/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
