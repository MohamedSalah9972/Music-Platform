from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Album

class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist', 'name', 'release_datetime', 'cost', 'is_approved']



