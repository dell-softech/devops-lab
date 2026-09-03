import os

os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from app import create_app


def test_home():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"DevOps Task App"


def test_health():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}