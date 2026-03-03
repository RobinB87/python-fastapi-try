from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_query_item_by_id():
    response = client.get("/items/1")
    assert response.status_code == 200

def test_query_item_by_id_returns_404():
    response = client.get("/items/3")
    assert response.status_code == 404

def test_query_item_by_parameters():
    response = client.get("/items/?name=Nails")
    assert response.status_code == 200