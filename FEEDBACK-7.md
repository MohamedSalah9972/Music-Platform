# Django Training - 7. Testing using Pytest

## Grade 80/100

## Task
3. Create a global fixture `auth_client` that returns a function, if that function is passed a user instance, it'll return an instance of DRF's `APIClient` authenticated by that user instance, otherwise, it'll return an instance of `APIClient` authenticated by an arbitrary user instance.
    * **(-10) The fixture should return a callable, here's one way to do it:**
        ```
        @pytest.fixture()
        def auth_client(db):
            """
            Returns a function that accepts a user model instance and returns REST Framework APIClient
            instance authenticated by the passed user instance, if no user instance is provided,
            the returned APIClient is authenticated by an arbitrary user instance
            """

            def _auth_client(user=None):
                client = APIClient()
                auth_user = user if user else UserFactory()
                client.force_authenticate(user=auth_user)
                return client

            return _auth_client
        ``` 

## Guidelines
7. **Code organization:**
    * **(-5) Organize your related tests into classes:**
    ```
    class TestArtistEndpoint
        def test_permissions(self, ...):
            ...
        def test_create_artist_with_valid_data(self, ...):
            ...
        def test_create_artist_with_invalid_data(self, ...):
            ...
    ```
    * **(-5) Use `reverse()` instead of hard coding the url**
    ```
    url = reverse("users:detail", kwargs={"pk": user.id}
    ```
    * **Tip: instead of creating fixtures that return instances of your models, use `FactoryBoy`**