# Django Training - 3. Forms, Templates, and Views

## Grade 85/100

## Task
1. Instead of having an explicit `created_at` field in the `Album` model, inherit from [`TimeStampedModel`](https://django-model-utils.readthedocs.io/en/latest/models.html#timestampedmodel) **(-5) remove the explicit `creation_datetime` field since it's already being replaced by `TiemStampedModel.created` field, make sure to update the references for the outdated field, anywhere you use `creation_datetime` replace it with `created`**
2. Create a form that allows a user to create an artist (it should be available at http://localhost:8000/artists/create)
    * **(-15) your urls aren't organized by common parent paths, here's one way to organize them:**

    ```
    # in base music_platform/urls.py 

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('artists/', include('artists.urls')),
        path('ablums/', include('albums.urls')),
    ]
    ```

    ```
    # in artists/urls.py

    from django.urls import path
    from . import views

    urlpatterns = [
            path('create/', views.create_artist, name='create_artists'),
            path('', views.ArtistsDetailView.as_view(), name="article-list"),

    ]
    ```

    ```
    # in albums/urls.py
    ...
    ```
3. Create a form that allows a user to create an album (it should be available at https://localhost:8000/albums/create)
    * (bonus) can you use a user friendly date/time input widget for the release datetime field instead of a plain text input field? **(+5)** 