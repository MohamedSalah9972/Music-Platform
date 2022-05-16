import pytest
from authentication.serializers import RegisterSerializer
from rest_framework.test import APIClient


@pytest.fixture
def user():
    user_dc = dict(
        username="mohamed",
        email="mohamed@example.com",
        password="123456mM@",
        confirmation_password="123456mM@",
        bio="I am Mohammed",
    )
    serializer = RegisterSerializer(data=user_dc)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return user


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def auth_client(user, client):
    login_credentials = dict(
        username="mohamed",
        password="123456mM@",
    )
    client.post('/authentication/login/', login_credentials)
    return client
