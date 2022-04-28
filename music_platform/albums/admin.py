from django.contrib import admin
from django.forms import ModelForm, models
from django import forms
from imagekit.admin import AdminThumbnail

from .models import Album, Song


class AlbumForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['is_approved'].help_text = 'Approve the album if its name is not explicit'

    class Meta:
        model = Album
        exclude = ()


class SongInlineFormset(models.BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            try:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    count += 1
            except AttributeError:
                pass
        if count < 1:
            raise forms.ValidationError('You must have at least one Song')


class SongInline(admin.StackedInline):
    model = Song
    extra = 0
    min_num = 1
    formset = SongInlineFormset


class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    inlines = [
        SongInline,
    ]


class SongAdmin(admin.ModelAdmin):
    pass


admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
