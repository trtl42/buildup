# Generated by Django 4.0.3 on 2023-05-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_position_person_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='team',
            field=models.IntegerField(max_length=1, null=True),
        ),
    ]
