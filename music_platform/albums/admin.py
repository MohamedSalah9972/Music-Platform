from django.contrib import admin
from django.forms import ModelForm
from imagekit.admin import AdminThumbnail

from .models import Album, Song


class AlbumForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['is_approved'].help_text = 'Approve the album if its name is not explicit'

    class Meta:
        model = Album
        exclude = ()


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_datetime',)
    form = AlbumForm


class AlbumInline(admin.StackedInline):  # which is better, StackedInline or TabularInline?
    model = Album

class SongAdmin(admin.ModelAdmin):
    pass
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
