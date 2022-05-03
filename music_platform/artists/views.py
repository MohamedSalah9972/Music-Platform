from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Artist


@method_decorator(login_required, name='dispatch')
class ArtistCreateView(CreateView):
    model = Artist
    fields = ['stage_name', 'social_link']

    def get_success_url(self):
        return reverse('artist-list')


class ArtistsDetailView(ListView):
    model = Artist
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artist_list'] = Artist.objects.prefetch_related('albums')
        # how can I get the same result using related_select instead of prefetch_related
        return context
