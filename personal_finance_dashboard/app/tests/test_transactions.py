from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_transaction():
    token = client.post("/auth/login", json={"email": "testuser@example.com", "password": "password123"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post("/transactions/", json={
        "type": "expense",
        "category": "Food",
        "amount": 20.5,
        "date": "2025-03-15",
        "description": "Lunch"
    }, headers=headers)
    
    assert response.status_code == 200
