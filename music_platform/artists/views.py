from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ArtistForm
from .models import Artist
from albums.models import Album


def create_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_artists')
    else:
        form = ArtistForm()
    return render(request, 'artist.html', {'form': form})


class ArtistCreateView(CreateView):
    model = Artist
    fields = ['stage_name', 'social_link']


class ArtistsDetailView(ListView):
    model = Artist
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artist_list'] = Artist.objects.prefetch_related('albums')
        # how can I get the same result using related_select instead of prefetch_related
        return context
