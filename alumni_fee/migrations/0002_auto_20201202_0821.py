# Generated by Django 2.2.10 on 2020-12-02 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_fee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni_fee',
            name='registration_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='alumni_fee',
            name='yearly_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]