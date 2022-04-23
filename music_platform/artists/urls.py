from django.urls import path
from . import views
urlpatterns = [
    path('artists/create/', views.create_artist, name='create_artists'),
    path('artists/', views.ArtistsDetailView.as_view(), name="article-list"),

]