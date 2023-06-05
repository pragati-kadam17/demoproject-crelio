# Generated by Django 4.2.1 on 2023-05-31 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_user_is_staff_user_is_superuser_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.patient')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.test')),
            ],
        ),
    ]
