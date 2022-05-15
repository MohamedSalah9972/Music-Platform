from django.urls import path

from .views import user_list, UserAPIView

urlpatterns = [
    path('', user_list, ),
    path('<int:pk>/', UserAPIView.as_view(), ),
]
