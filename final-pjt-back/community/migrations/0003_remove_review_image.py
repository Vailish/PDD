# Generated by Django 3.2.13 on 2022-11-20 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_review_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
    ]
