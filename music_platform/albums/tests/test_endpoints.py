import json

import pytest
from django.urls import reverse


class TestAlbumEndpoints:
    @pytest.mark.django_db
    def test_post_album(self, auth_client, artist):
        payload = dict(
            artist=1,
            name="Album",
            release_datetime="2022-05-29",
            cost="5.00",
            is_approved=True
        )
        url = reverse('album_list_create')
        response = auth_client.post(url, json.dumps(payload), content_type='application/json')
        #  please remove unused comments, like prints
        print(payload, response.data) 
        # why testing 200 or 201 ?
        assert response.status_code == 201 or response.status_code == 200
        assert response.data['artist'] == payload['artist']
        # please use factories again
        payload['id'] = response.data['id']  # Add id for valid comparison
        assert response.data == payload

    @pytest.mark.django_db
    def test_post_album_unauthenticated(self, client, artist):
        # you can use an  object and pass data=data for the post function with format="json"
        payload = dict(
            artist=1,
            name="Album",
            release_datetime="2022-05-29",
            cost="5.00",
            is_approved=True
        )
        url = reverse('album_list_create')
        response = client.post(url, payload, content_type='application/json')
        assert response.status_code == 400  # why didn't check the permissions and return 403 not 400?

    @pytest.mark.django_db
    def test_post_album_missing_field(self, auth_client, artist):
        payload = dict(
            name="Album",
            release_datetime="2022-05-29",
            cost="5.00",
            is_approved=True
        )
        url = reverse('album_list_create')
        response = auth_client.post(url, json.dumps(payload), content_type='application/json')
        print(payload, response.data)
        assert response.status_code == 400

    # you should test getting only approved albums
    @pytest.mark.django_db
    def test_get_album(self, client, album):
        url = reverse('album_list_create')
        response = client.get(url)
        assert response.status_code == 200

