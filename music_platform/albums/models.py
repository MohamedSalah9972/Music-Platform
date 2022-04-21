from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel

from django.utils import timezone


class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)  # on_delete=models.CASCADE ??
    name = models.CharField(max_length=32, default='New Album')
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateField(blank=False)
    cost = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    is_approved = models.BooleanField(default=False)
