# Generated by Django 4.0.3 on 2023-06-01 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_remove_person_stand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pots',
            name='pot_id',
            field=models.CharField(max_length=3, null=True),
        ),
    ]