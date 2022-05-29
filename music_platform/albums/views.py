from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from artists.models import Artist
from .models import Album
from .serializers import AlbumSerializer, AlbumPostSerializer


@method_decorator(login_required, name='dispatch')
class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist', 'name', 'release_datetime', 'cost', 'is_approved']

    def get_success_url(self):
        return reverse('artist-list')


class AuthenticatedArtist(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == 'POST':
            # is it better to add 'is_artist' to objects manager of user (e.g. user.is_artist()) ?
            if request.user.is_anonymous or not Artist.objects.filter(user=request.user).exists():
                raise PermissionDenied()

        return True


class AlbumViewSet(generics.GenericAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.AllowAny, AuthenticatedArtist]

    def get(self, request, format=None):
        artists = Album.objects.approved_albums().all()
        serializer = AlbumSerializer(artists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlbumPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
