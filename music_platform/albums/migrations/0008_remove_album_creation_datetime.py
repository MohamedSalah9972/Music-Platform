# Generated by Django 4.0.3 on 2022-04-28 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0007_song_audio_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='creation_datetime',
        ),
    ]
