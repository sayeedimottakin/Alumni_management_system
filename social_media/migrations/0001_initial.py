# Generated by Django 2.2.10 on 2020-11-05 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumni_profile', '0005_auto_20201029_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('image', models.FileField(blank=True, upload_to='uploads/')),
                ('files', models.FileField(blank=True, upload_to='uploads/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(choices=[('Job Circular', 'Job Circular'), ('Educational Blog', 'Educational Blog'), ('Higher Study Opportunities', 'Higher Study Opportunities'), ('Publications', 'Publications'), ('Achievements', 'Achievements')], max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumni_profile.Alumni_Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('image', models.FileField(blank=True, upload_to='uploads/')),
                ('files', models.FileField(blank=True, upload_to='uploads/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumni_profile.Alumni_Profile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_media.Post')),
            ],
        ),
    ]