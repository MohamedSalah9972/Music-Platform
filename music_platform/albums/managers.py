from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.functions import Coalesce
from django.apps import apps


class AlbumCustomManager(models.QuerySet):
    def approved_albums(self):
        Album = apps.get_model("albums", 'Album')
        return Album.objects.filter(is_approved=True)
