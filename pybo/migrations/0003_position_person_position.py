# Generated by Django 4.0.3 on 2023-05-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_person_stand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.IntegerField(null=True),
        ),
    ]