from django.shortcuts import render, get_object_or_404

from django.contrib.auth import login, user_logged_out
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import permissions, generics, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, CustomUserSerializer, LoginUserSerializer

from users.models import CustomUser


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginUserSerializer
    authentication_classes = [TokenAuthentication]

    def post(self, request, format=None):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)[1]

        login(request, user)
        return Response({
            "token": token,
            "user": CustomUserSerializer(user).data
        })


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)[1]
        return Response({
            "token": token,
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data
        })


