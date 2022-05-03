from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.ArtistCreateView.as_view(), name='create_artists'),
    path('', views.ArtistsDetailView.as_view(), name="artist-list"),

]