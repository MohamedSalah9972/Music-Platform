import pytest
from users import models


@pytest.mark.django_db
def test_user_get(user, client):
    response = client.get(f"/users/{user.id}/")
    assert response.data["user"]["id"] == user.id
    assert response.data["user"]["username"] == user.username
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_get_not_found(client):
    response = client.get(f"/users/{0}/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_user_put(user, auth_client):
    payload = dict(
        username="x",
        email="exw@ppp.com",
        bio="new bio",
    )
    response = auth_client.put(f"/users/{user.id}/", payload)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_unauthorized(user, client):
    payload = dict(
        username="x",
        email="emad@gmail.com",
        bio="new bio",
    )
    response = client.put(f"/users/{user.id}/", payload)
    assert response.status_code == 401


@pytest.mark.django_db
def test_user_put_invalid_permission(user, auth_client):
    payload = dict(
        username="x",
        email="new@new.com",
        bio="new bio",
    )

    models.CustomUser.objects.create_user("mo", "ahmed@ggg.com", "123456mM@")
    response = auth_client.put(f"/users/{2}/", payload)
    assert response.status_code == 403


@pytest.mark.django_db
def test_user_put_missing_field(user, auth_client):
    payload = dict(
        username="x",
        bio="new bio",
    )

    response = auth_client.put(f"/users/{user.id}/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_user_patch(user, auth_client):
    payload = dict(
        username="x",
        email="exw@ppp.com",
        bio="new bio",
    )
    response = auth_client.patch(f"/users/{user.id}/", payload)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_patch_unauthorized(user, client):
    payload = dict(
        username="x",
        bio="new bio",
    )
    response = client.patch(f"/users/{user.id}/", payload)
    assert response.status_code == 401


@pytest.mark.django_db
def test_user_patch_invalid_permission(user, auth_client):
    payload = dict(
        username="x",
        email="new@new.com",
        bio="new bio",
    )

    models.CustomUser.objects.create_user("mo", "ahmed@ggg.com", "123456mM@")
    response = auth_client.patch(f"/users/{2}/", payload)
    assert response.status_code == 403


@pytest.mark.django_db
def test_user_patch_missing_field(user, auth_client):
    payload = dict(
        username="x",
        bio="new bio",
    )

    response = auth_client.patch(f"/users/{user.id}/", payload)
    assert response.status_code == 200
