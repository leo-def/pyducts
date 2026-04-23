from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Pyducts Architecture Model"

def test_create_product_success():
    payload = {
        "title": "Test Product",
        "description": "Description",
        "price": 100.0
    }
    response = client.post("/products", json=payload)
    assert response.status_code == 200 # Actual HTTP status is 200 as configured in ResponseDTO
    data = response.json()
    assert data["status"] == 201
    assert data["data"]["title"] == "Test Product"
    assert "EFF_NOTIFY_ADMIN" in data["effects"]

def test_create_product_validation_error():
    payload = {
        "title": "Error Product",
        "description": "Negative Price",
        "price": -10.0
    }
    response = client.post("/products", json=payload)
    data = response.json()
    assert data["status"] == 400
    assert data["errors"][0]["code"] == "PROD_001"
