# Generated by Django 3.2.13 on 2022-11-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='popularity',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='popularity',
            field=models.FloatField(null=True),
        ),
    ]
