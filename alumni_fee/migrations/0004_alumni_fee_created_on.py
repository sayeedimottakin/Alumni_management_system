# Generated by Django 2.2.10 on 2020-12-09 03:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_fee', '0003_auto_20201202_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni_fee',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
