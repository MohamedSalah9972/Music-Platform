from django.shortcuts import render
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from rest_framework import permissions, status, generics, viewsets, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from authentication.serializers import CustomUserSerializer
from .models import CustomUser
from .permissions import IsOwnerOrReadOnly


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):

    def get_object(self):
        obj = get_object_or_404(CustomUser.objects.all(), pk=self.request.data['id'])
        return obj

    queryset = CustomUser.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(CustomUser.objects.all(), pk=pk)
        return Response({
            "user": CustomUserSerializer(user).data
        })

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        url_pk = self.kwargs.get('pk')
        user_pk = self.request.data['id']
        if url_pk != user_pk:
            raise serializers.ValidationError({"detail": "You do not have permission to perform this action."})

        serializer = CustomUserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        url_pk = self.kwargs.get('pk')
        user_pk = self.request.data['id']
        if url_pk != user_pk:
            raise serializers.ValidationError({"detail": "You do not have permission to perform this action."})

        user_response = self.partial_update(request, *args, **kwargs)
        return Response({
            "user": user_response.data
        })


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def user_list(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def user_detail(request, pk):
#     user = get_object_or_404(CustomUser.objects.all(), pk=pk)
#     token, created = Token.objects.get_or_create(user=user)
#     serializer = CustomUserSerializer(user, many=False)
#     return Response({"token": token.key,
#                      "user": serializer.data})
