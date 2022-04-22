from django.urls import path
from . import views
urlpatterns = [
    path('albums/create/', views.create_album, name='create_albums'),
]