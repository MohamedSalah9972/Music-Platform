from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.validators import FileExtensionValidator

from django.utils import timezone
from django.conf import settings
from .managers import AlbumCustomManager


class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)  # on_delete=models.CASCADE ??
    name = models.CharField(max_length=32, default='New Album')
    release_datetime = models.DateField(blank=False)
    cost = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    is_approved = models.BooleanField(default=False)
    objects = AlbumCustomManager.as_manager()


class Song(TimeStampedModel):
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=True, null=True)
    img = models.ImageField(null=False, upload_to='images')
    img_thumbnail = ImageSpecField(source='img',
                                   format='JPEG',
                                   options={'quality': 60})

    audio_file = models.FileField(upload_to='audio',
                                  validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])

    def save(self, *args, **kwargs):
        print(settings.STATIC_URL)
        if not self.name:
            self.name = self.album.name
        super(Song, self).save(*args, **kwargs)
