# Generated by Django 5.0 on 2023-12-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_blogger_profile_viewer_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger_profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='viewer_profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
