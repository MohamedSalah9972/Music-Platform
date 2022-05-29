from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Album
from .serializers import AlbumSerializer


@method_decorator(login_required, name='dispatch')
class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist', 'name', 'release_datetime', 'cost', 'is_approved']

    def get_success_url(self):
        return reverse('artist-list')


class AlbumViewSet(generics.GenericAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        print(request)
        return True

    def get(self, request, format=None):
        artists = Album.objects.approved_albums().all()
        serializer = AlbumSerializer(artists, many=True)
        return Response(serializer.data)
