# Generated by Django 4.0.3 on 2023-05-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0004_team_person_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='team',
            field=models.IntegerField(null=True),
        ),
    ]
