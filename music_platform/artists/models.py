from django.db import models
from django.conf import settings
from .managers import ArtistQuerySet


class Artist(models.Model):
    stage_name = models.CharField(max_length=128, null=False, blank=False, unique=True)
    social_link = models.URLField(max_length=128, null=False, blank=True, default='')
    objects = ArtistQuerySet.as_manager()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['stage_name']  # ascending
