from django.contrib import admin

from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artist, ArtistAdmin)
