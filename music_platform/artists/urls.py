from django.urls import path
from . import views
urlpatterns = [
    path('artists/create/', views.ArtistCreateView.as_view(), name='create_artists'),
    path('artists/', views.ArtistsDetailView.as_view(), name="article-list"),

]