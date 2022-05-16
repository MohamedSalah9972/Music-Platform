import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_register_user():
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
def test_register_user_missing_field():
    payload = dict(
        username="mohamed",
        password="123456mM@",
        confirmation_password="123456mM@",
        bio="I am Mohammed",
    )

    response = client.post('/authentication/register/', payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_login_user(user):
    login_credentials = dict(
        username="mohamed",
        password="123456mM@",
    )
    response = client.post('/authentication/login/', login_credentials)

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail():
    login_credentials = dict(
        username="mohamed",
        password="123456mM@",
    )
    response = client.post('/authentication/login/', login_credentials)

    assert response.status_code == 400
