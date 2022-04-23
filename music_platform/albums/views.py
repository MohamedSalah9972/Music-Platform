from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView

from .forms import AlbumForm
from .models import Artist


def create_album(request):
    form = AlbumForm
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_albums')

    return render(request, "albums.html", {'form': form})




