from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

basePath = '/items'

def test_root():
    response = client.get(basePath)
    assert response.status_code == 200

def test_query_item_by_id():
    response = client.get(f"{basePath}/1")
    assert response.status_code == 200

def test_query_item_by_id_returns_404():
    response = client.get(f"{basePath}/3")
    assert response.status_code == 404

def test_query_item_by_parameters():
    response = client.get(f"{basePath}/?name=Nails")
    assert response.status_code == 200

def test_add_item():
    response = client.post(basePath, json={
        "name": "Screwdriver",
        "price": 3.99,
        "count": 10,
        "id": 3,
        "category": "tools"
    })
    assert response.status_code == 200
    assert response.json()["added"]["name"] == "Screwdriver"