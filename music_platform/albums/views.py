from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from .models import Album


@method_decorator(login_required, name='dispatch')
class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist', 'name', 'release_datetime', 'cost', 'is_approved']

    def get_success_url(self):
        return reverse('artist-list')
