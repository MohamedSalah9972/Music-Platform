from django.contrib import admin
from django.db.models import Count, Q

from .models import Artist
from albums.models import Album


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'approved_albums')

    def approved_albums(self, artist):  # should I make this function static ?
        num_of_approved = Album.objects.filter(artist=artist, is_approved=True).count()
        return num_of_approved

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _approved_albums=Count("albums", filter=Q(albums__is_approved=True)),
        )
        return queryset

    approved_albums.admin_order_field = '_approved_albums'


admin.site.register(Artist, ArtistAdmin)
