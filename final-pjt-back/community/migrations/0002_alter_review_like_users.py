# Generated by Django 3.2.13 on 2022-11-18 07:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='like_users',
            field=models.ManyToManyField(null=True, related_name='like_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
