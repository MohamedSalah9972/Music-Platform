# Generated by Django 4.0.4 on 2022-05-16 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_myuser_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]