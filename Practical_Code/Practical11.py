from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Welcome to Student API"
    }

def test_get_students():
    
    response = client.get("/students")

    assert response.status_code == 200

    assert len(response.json()) > 0

def test_get_existing_student():
    
    response = client.get("/students/1")

    assert response.status_code == 200

    assert response.json()["name"] == "Rahul"
