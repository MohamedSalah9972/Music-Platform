from django.contrib import admin
from .models import Album


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_datetime',)


admin.site.register(Album, AlbumAdmin)
