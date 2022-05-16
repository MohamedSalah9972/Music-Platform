import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_user(client):
    payload = dict(
        username="mohamed",
        email="mohamed@example.com",
        password="123456mM@",
        confirmation_password="123456mM@",
        bio="I am Mohammed",
    )

    response = client.post('/authentication/register/', payload)
    user = response.data["user"]
    assert user["username"] == payload["username"]
    assert "password" not in user
    assert user["email"] == payload["email"]
    assert response.status_code == 200


@pytest.mark.django_db
def test_register_user_missing_field(client):
    payload = dict(
        username="mohamed",
        password="123456mM@",
        confirmation_password="123456mM@",
        bio="I am Mohammed",
    )

    response = client.post('/authentication/register/', payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_login_user(user, client):
    login_credentials = dict(
        username="mohamed",
        password="123456mM@",
    )
    response = client.post('/authentication/login/', login_credentials)
    assert response.status_code == 200
    assert response.data["user"]["id"] == user.id


@pytest.mark.django_db
def test_login_user_fail(client):
    login_credentials = dict(
        username="mohamed",
        password="123456mM@",
    )
    response = client.post('/authentication/login/', login_credentials)

    assert response.status_code == 400
