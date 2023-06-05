# Generated by Django 4.2.1 on 2023-05-30 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_labheadsignup_patientsignup'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='default_username', max_length=150, unique=True),
        ),
    ]