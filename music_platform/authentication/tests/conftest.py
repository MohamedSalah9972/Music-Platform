import pytest
from authentication.serializers import RegisterSerializer


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
