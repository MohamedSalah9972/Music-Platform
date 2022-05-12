
from django.urls import path

from users.views import UserDetailView

urlpatterns = [
    path('', UserDetailView.as_view()),
]
