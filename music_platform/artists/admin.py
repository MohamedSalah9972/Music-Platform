from django.contrib import admin

from .models import Artist
from albums.models import Album


class ArtistAdmin(admin.ModelAdmin):
    def approved_count(self, artist):  # should I make this function static ?
        num_of_approved = Album.objects.filter(artist=artist, is_approved=True).count()
        return num_of_approved

    list_display = ('stage_name', 'approved_count')


admin.site.register(Artist, ArtistAdmin)
