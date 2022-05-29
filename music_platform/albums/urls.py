from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.AlbumCreateView.as_view(), name='create_albums'),
    path('', views.AlbumViewSet.as_view(), name='album_view_set')
]