# Generated by Django 2.2.10 on 2021-01-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_profile', '0008_auto_20210101_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni_profile',
            name='social_media_links',
            field=models.URLField(blank=True),
        ),
    ]
