from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.functions import Coalesce
from django.apps import apps


class ArtistQuerySet(models.QuerySet):
    def with_approved_albums(self):
        Album = apps.get_model("albums", "Album")  # to avoid 'partially initialized module' error

        subquery = (
            Album.objects.filter(artist=models.OuterRef("pk")).values("artist")
                .annotate(approved_albums_sum=models.Sum("approved")).values("approved_albums_sum")
        )  # the result of this will look something like [{artist1, 0}, {artist2, 15}, {artist3, None}]

        # we use Coalesce because the subquery could be `None` for the artists who have no albums
        return self.annotate(approved_albums=Coalesce(
            models.Subquery(subquery),
            0,
            output_field=IntegerField(),
        ))
