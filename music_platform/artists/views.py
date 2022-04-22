from django.shortcuts import render, redirect

from .forms import ArtistForm

def create_artist(request):
    form = ArtistForm
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('create_artists')

    return render(request, 'artist.html', {'form':form})