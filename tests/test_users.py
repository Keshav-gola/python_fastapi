from app import schemas
import pytest
from jose import jwt
from app.config import settings




# def test_root(client):
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello World"}

def test_create_usser(client):
    response = client.post("/users/", json={"email": "helloworld@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**response.json())
    assert response.status_code == 201
    assert new_user.email == "helloworld@gmail.com"

def test_login_user(client, test_user):
    res = client.post(
        "/login", data={"username": test_user["email"], "password": test_user["password"]}
    )
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert res.status_code == 200

