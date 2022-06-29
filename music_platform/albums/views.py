import numbers

from django.contrib.auth.decorators import login_required
from django.core import exceptions
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied, ParseError, ValidationError as RestValidationError, NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from artists.models import Artist
from .models import Album
from .serializers import AlbumSerializer, AlbumPostSerializer
from django_filters import rest_framework as filters


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


class AlbumFilter(filters.FilterSet):
    cost__gte = filters.NumberFilter(field_name="cost", lookup_expr='gte')
    cost__lte = filters.NumberFilter(field_name="cost", lookup_expr='lte')
    name = filters.CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = Album
        fields = ['cost__gte', 'cost__lte', 'name']


class AlbumListCreateAPI(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer
    # due to precedence the last class is not used
    permission_classes = [permissions.AllowAny, AuthenticatedArtist]
    filterset_class = AlbumFilter
    
    def get_queryset(self):
        return Album.objects.approved_albums().all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AlbumPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CustomFilter:
    errors = {}

    def filter(self, queryset, query_params):
        self.errors.clear()
        for key in query_params:
            try:
                queryset = queryset.filter(**{key: query_params[key]})  # is this the best optimized queries?
            except exceptions.ValidationError as e:
                self.errors[key] = list(e)

        if self.errors:
            raise RestValidationError(self.errors)

        return queryset


class GetCustomFilter(generics.ListAPIView, CustomFilter):
    serializer_class = AlbumSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Album.objects.approved_albums().all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter(self.get_queryset(), request.query_params)
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)
