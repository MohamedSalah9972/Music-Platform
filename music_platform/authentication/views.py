from django.shortcuts import render

from django.contrib.auth import login
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework import permissions, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import RegisterSerializer, CustomUserSerializer, LoginUserSerializer

from users.models import CustomUser


class LoginAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [TokenAuthentication]
    serializer_class = LoginUserSerializer

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token = AuthToken.objects.create(user)[1]
        return Response({
            "token": token,
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data
        })


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

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


# class CustomAuthToken(ObtainAuthToken):
#     authentication_classes = [TokenAuthentication]
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
#         })
