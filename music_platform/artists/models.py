from django.db import models

from .managers import ArtistQuerySet


class Artist(models.Model):
    stage_name = models.CharField(max_length=128, null=False, blank=False, unique=True)
    social_link = models.URLField(max_length=128, null=False, blank=True, default='')
    objects = ArtistQuerySet.as_manager()
    
    class Meta:
        ordering = ['stage_name']  # ascending
