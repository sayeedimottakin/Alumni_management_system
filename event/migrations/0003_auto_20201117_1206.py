# Generated by Django 2.2.10 on 2020-11-17 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_profile', '0007_auto_20201115_1143'),
        ('event', '0002_event_is_present'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('alumni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumni_profile.Alumni_Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('discipline', models.CharField(blank=True, choices=[('Architecture', 'Architecture'), ('CSE', 'CSE'), ('ECE', 'ECE'), ('Math', 'Math'), ('URP', 'URP'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Stat', 'Stat'), ('Pharmacy', 'Pharmacy'), ('BGE', 'BGE'), ('FWT', 'FWT'), ('FMRT', 'FMRT'), ('Agrotechnology', 'Agrotechnology'), ('ES', 'ES'), ('SWE', 'SWE'), ('BAD', 'BAD'), ('HRM', 'HRM'), ('DP', 'DP'), ('PM', 'PM'), ('DS', 'DS'), ('History', 'History'), ('English', 'English'), ('Bangla', 'Bangla'), ('IER', 'IER'), ('Sculpture', 'Sculpture'), ('Econ', 'Econ'), ('Sociology', 'Sociology'), ('MCJ', 'MCJ'), ('Law', 'Law')], max_length=255)),
                ('visible_to', models.CharField(blank=True, choices=[('Architecture', 'Architecture'), ('CSE', 'CSE'), ('ECE', 'ECE'), ('Math', 'Math'), ('URP', 'URP'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Stat', 'Stat'), ('Pharmacy', 'Pharmacy'), ('BGE', 'BGE'), ('FWT', 'FWT'), ('FMRT', 'FMRT'), ('Agrotechnology', 'Agrotechnology'), ('ES', 'ES'), ('SWE', 'SWE'), ('BAD', 'BAD'), ('HRM', 'HRM'), ('DP', 'DP'), ('PM', 'PM'), ('DS', 'DS'), ('History', 'History'), ('English', 'English'), ('Bangla', 'Bangla'), ('IER', 'IER'), ('Sculpture', 'Sculpture'), ('Econ', 'Econ'), ('Sociology', 'Sociology'), ('MCJ', 'MCJ'), ('Law', 'Law')], max_length=255)),
                ('target_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('present_amount', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('is_present', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='contributers',
        ),
        migrations.DeleteModel(
            name='Contributer',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.AddField(
            model_name='contributers',
            name='event_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.Events'),
        ),
    ]