from django import forms
from django.forms import DateInput
from django.contrib.admin import widgets

from .models import Album


class AlbumForm(forms.ModelForm):
    release_datetime = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Album
        fields = ['artist', 'name', 'release_datetime', 'cost', 'is_approved']
