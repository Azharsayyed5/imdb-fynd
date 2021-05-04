from fastapi.testclient import TestClient
from .server.app import app

client = TestClient(app)

success_data = {
  "audioFileType": "audiobook",
  "audioFileMetaData": {
    "uploaded_time": "2021-03-13 16:20:20",
    "duration_time": 120,
    "title": "happy happy x1",
    "author": "azhar",
    "narrator": "mr whites"
  }
}

failure_data = {
  "audioFileType": "audiobook",
  "audioFileMetaData": {
    "uploaded_time": "2021-03-13 16:20:20",
    "duration_time": 120,
    "title": "happy happy x1",
    "author": "azhar",
  }
}

failure_data_2 = {
  "audioFileType": "audiobook",
  "audioFileMetaData": {
    "uploaded_time": "2021-03-13 16:20:20",
    "duration_time": 0,
    "title": "happy happy x1",
    "author": "azhar",
    "narrator": "mr whites"
  }
}

failure_data_3 = {
  "audioFileType": "podcast",
  "audioFileMetaData": {
    "uploaded_time": "2021-03-13 16:20:20",
    "duration_time": 0,
    "name": "aaaaaaa",
    "host": "azhar",
    "participents": ["a", "b", "c", "d", "e", "f","g","h","i", "k", "l", "w"]
  }
}

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to this fantastic app!"}

def test_create_song():
    response = client.post("/v1/filed/", json=success_data)
    assert response.status_code == 200

def test_create_song_fail():
    response = client.post("/v1/filed/", json=failure_data)
    assert response.json()["code"] == 400
    assert response.json()["message"] == "please check missing fields in the request body."

def test_create_song_fail_2():
    response = client.post("/v1/filed/", json=failure_data_2)
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Please check audio duration, it should be greater than 1 second."

def test_get_all():
    response = client.get("/v1/filed/song/")
    assert response.json()["code"] == 200

def test_get_one():
    response = client.get("/v1/filed/song/606881f7830e68ae454d717d")
    assert response.json()["code"] == 400

def test_delete():
    response = client.get("/v1/filed/song/606881f7830e68ae454d717d")
    assert response.json()["code"] == 400

def test_create_participents():
    response = client.post("/v1/filed/", json=failure_data_3)
    assert response.json()["code"] == 400

def test_delete_two():
    response = client.get("/v1/filed/wrong_type/606881f8830e68ae454d717d")
    assert response.json()["code"] == 400