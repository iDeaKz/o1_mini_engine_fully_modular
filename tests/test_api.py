import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Sword", "description": "A sharp blade.", "price": 100.0})
    assert response.status_code == 201
    assert response.json()["name"] == "Sword"

def test_get_item_not_found():
    response = client.get("/items/NonExistentItem")
    assert response.status_code == 404
