from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.AlbumCreateView.as_view(), name='create_albums'),
]