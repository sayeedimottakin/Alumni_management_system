# Generated by Django 2.2.10 on 2021-01-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20210119_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_letter',
        ),
        migrations.AddField(
            model_name='news',
            name='news_letter',
            field=models.ManyToManyField(blank=True, null=True, related_name='news', to='news.News_Letter'),
        ),
    ]
