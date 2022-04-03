from django.db import models
from artists.models import Artist
from django.utils import timezone


class Album(models.Model):
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)  # on_delete=models.CASCADE ??
    name = models.CharField(max_length=32, default='New Album')
    creation_datetime = models.DateTimeField(default=timezone.now)
    release_datetime = models.DateTimeField(blank=False)
    cost = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
