from django.urls import path
from .views import AlbumCreateView, AlbumListCreateAPI, GetCustomFilter

urlpatterns = [
    path('create/', AlbumCreateView.as_view(), name='create_albums'),  ##
    path('', AlbumListCreateAPI.as_view(), name='album_list_create'),
    path('custom/', GetCustomFilter.as_view(), name='get_custom_filter'),
]
