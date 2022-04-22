from django import forms
from .models import Artist


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['stage_name', 'social_link']
