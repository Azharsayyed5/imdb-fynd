from fastapi.testclient import TestClient
import sys
import os
from pathlib import Path
sys.path.append(os.path.dirname(Path(os.path.abspath(__file__))))
from server.app import app

client = TestClient(app)

movie_data = {
    "popularity": 99,
    "director": "Cristopher nolan",
    "genre": [
      "thriller",
      "action"
    ],
    "imdb_score": 9.6,
    "name": "The dark knight"
}

login_data = {
    "email": "arizsayed777@gmail.com",
    "password": "123456"
}

login_data_failed = {
    "email": "dummy@gmail.com",
    "password": "wrong_password"
}

def test_login():
    response = client.post("/v1/accounts/login", json=login_data)
    assert response.status_code == 200

def test_login_failed():
    response = client.post("/v1/accounts/login", json=login_data_failed)
    assert response.status_code == 404

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to IMBD!"}

def test_create_movie():
    response = client.post("/v1/accounts/login", json=login_data)
    assert response.status_code == 200
    resp = response.json()
    headers = {"Authorization": f"Bearer {resp['access_token']}"}
    response = client.post("/v1/imdb/movies", json=movie_data, headers=headers)
    assert response.status_code == 200

def test_search_one():
    
    response = client.get("/v1/imdb/movies?search=batman")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 2

def test_search_two():
    response = client.get("/v1/imdb/movies?genre=action,thriller")
    assert response.status_code == 200
    assert response.json()["message"] == "Success"

def test_search_three():
    response = client.get("/v1/imdb/movies?p_srange=0&p_erange=10")
    assert response.status_code == 200
    assert response.json()["message"] == "Success"

def test_search_four():
    response = client.get("/v1/imdb/movies?p_srange=0")
    assert response.status_code == 400
    assert response.json()["detail"] == "Send start and end range for popularity filtering"

def test_search_five():
    response = client.get("/v1/imdb/movies?orderby=asc")
    assert response.status_code == 200
    assert response.json()["message"] == "Success"