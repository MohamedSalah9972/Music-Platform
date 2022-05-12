from django.shortcuts import render
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from rest_framework import permissions, status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import CustomUserSerializer
from .models import CustomUser


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self):
        return get_object_or_404(CustomUser, pk=self.request.data['id'])

    permission_classes = [permissions.AllowAny]
    authentication_classes = [TokenAuthentication]
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return Response({
            "token": AuthToken.objects.create(user)[1],
            "user": CustomUserSerializer(user).data
        })

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = CustomUserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        user_response = self.partial_update(request, *args, **kwargs)
        return Response({
            "token": AuthToken.objects.create(self.get_object())[1],
            "user": user_response.data
        })
