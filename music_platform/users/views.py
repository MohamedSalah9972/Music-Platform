from django.shortcuts import render
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from rest_framework import permissions, status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import CustomUserSerializer
from .models import CustomUser


class UserDetailView(generics.GenericAPIView):
    def get_object(self, pk):
        return get_object_or_404(CustomUser, pk=pk)

    permission_classes = [permissions.AllowAny]
    authentication_classes = [TokenAuthentication]

    queryset = CustomUser.objects.all()

    def get(self, request, *args, **kwargs):
        user = self.get_object(request.data['pk'])
        return Response({
            "token": AuthToken.objects.create(user)[1],
            "user": CustomUserSerializer(user).data
        })

    def put(self, request, *args, **kwargs):

        user = self.get_object(request.data['id'])

        serializer = CustomUserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
