# Generated by Django 4.0.3 on 2023-06-06 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0013_person_sp_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='sp_check',
        ),
    ]
