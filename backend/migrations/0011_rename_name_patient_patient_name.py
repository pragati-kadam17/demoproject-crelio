# Generated by Django 4.2.1 on 2023-06-01 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_rename_name_test_test_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='name',
            new_name='patient_name',
        ),
    ]
