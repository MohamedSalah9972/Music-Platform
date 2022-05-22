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
        obj = get_object_or_404(CustomUser.objects.all(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    queryset = CustomUser.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
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
        serializer = CustomUserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.validated_data['email'] = serializer.validated_data['email'].lower()
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        print(type(request.data))
        if 'email' in request.data:
            request.data['email'] = request.data['email'].lower()
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
