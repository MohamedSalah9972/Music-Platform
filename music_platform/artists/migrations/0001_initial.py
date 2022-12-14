# Generated by Django 4.0.3 on 2022-04-03 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=128, unique=True)),
                ('social_link', models.URLField(blank=True, default='', max_length=128)),
            ],
            options={
                'ordering': ['stage_name'],
            },
        ),
    ]
