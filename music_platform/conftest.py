import json

import pytest
from django.urls import reverse

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
    # i see this as a duplicate, please use factories
    login_credentials = dict(
        username="mohamed",
        password="123456mM@",
    )
    #  i don't see the point of this, can you explain more
    client.post('/authentication/login/', login_credentials)
    client.force_authenticate(user=user)
    return client

# search using factories to create instances
@pytest.fixture
def artist(auth_client):
    payload = dict(
        stage_name="newOne",
        social_link="https://socail.com",
        user=1
    )
    res = auth_client.post('/artists/', json.dumps(payload), content_type='application/json')
    return res

# i'm not sure you're testing this right, you're passing artist you don't use, just to have in the backend an artisit with id==1, imagine we have different way of setting the ids, it will fail, it's better to use  artist = artist.id

@pytest.fixture
def album(auth_client, artist):
    payload = dict(
        artist=1,
        name="Album",
        release_datetime="2022-05-29",
        cost="5.00",
        is_approved=True
    )
    url = reverse('album_list_create')
    response = auth_client.post(url, json.dumps(payload), content_type='application/json')
    return response
