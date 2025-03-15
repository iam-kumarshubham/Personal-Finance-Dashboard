from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup():
    response = client.post("/auth/signup", json={
        "email": "testuser@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "user_id" in response.json()

def test_login():
    response = client.post("/auth/login", json={
        "email": "testuser@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
