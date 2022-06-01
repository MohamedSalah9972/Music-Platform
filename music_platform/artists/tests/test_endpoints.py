import json

import pytest
# from rest_framework.test import APIClient
# from ..models import Artist
#
#
@pytest.mark.django_db
def test_post_artist(auth_client):
    payload = dict(
        stage_name="newOne",
        social_link="https://socail.com",
        user=1
    )
    res = auth_client.post('/artists/', json.dumps(payload), content_type='application/json')
    assert res.status_code == 200
    assert res.data['stage_name'] == payload['stage_name']

#
# @pytest.mark.django_db
# def test_post_artist_unauthenticated(client):
#     payload = dict(
#         stage_name="newOne",
#         social_link="https://socail.com"
#     )
#     res = client.post('/artists/', json.dumps(payload), content_type='application/json')
#     assert res.status_code == 401
#
#
# @pytest.mark.django_db
# def test_get_artist(artist, client):
#     res = client.get('/artists/')
#     assert res.status_code == 200
#     assert res.data[0]['id'] == artist.data['id']
#
