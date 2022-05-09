from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from rest_framework.response import Response

from .models import Artist
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ArtistSerializer


@method_decorator(login_required, name='dispatch')
class ArtistCreateView(CreateView):
    model = Artist
    fields = ['stage_name', 'social_link']

    def get_success_url(self):
        return reverse('artist-list')


class ArtistsDetailView(ListView):
    model = Artist
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artist_list'] = Artist.objects.prefetch_related('albums')
        # how can I get the same result using related_select instead of prefetch_related
        return context


from rest_framework import generics, status, views, permissions


class ArtistViewSet(generics.GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post']

    def get(self, request, format=None):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArtistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
