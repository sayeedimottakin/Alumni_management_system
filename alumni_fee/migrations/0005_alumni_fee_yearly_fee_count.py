# Generated by Django 2.2.10 on 2020-12-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_fee', '0004_alumni_fee_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni_fee',
            name='yearly_fee_count',
            field=models.IntegerField(default=0),
        ),
    ]
