import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "foo"
    assert "id" in data

def test_update_post():
    payload = {
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "updated title"

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
