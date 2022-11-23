# Generated by Django 3.2.13 on 2022-11-23 16:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('popularity', models.FloatField(null=True)),
                ('profile_path', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('character_name', models.CharField(max_length=100, null=True)),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters_id', to='movies.actor')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('popularity', models.FloatField(null=True)),
                ('profile_path', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('adult', models.BooleanField(null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('tagline', models.TextField(null=True)),
                ('overview', models.TextField(null=True)),
                ('poster_path', models.CharField(max_length=200, null=True)),
                ('backdrop_path', models.CharField(max_length=200, null=True)),
                ('popularity', models.FloatField(null=True)),
                ('release_date', models.DateField(null=True)),
                ('runtime', models.IntegerField(null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('trailer_youtube_key', models.TextField(null=True)),
                ('movie_similar', models.JSONField(blank=True)),
                ('actors', models.ManyToManyField(related_name='movies', through='movies.Characters', to='movies.Actor')),
                ('director', models.ManyToManyField(related_name='movies', to='movies.Director')),
                ('genre_ids', models.ManyToManyField(related_name='movies', to='movies.Genres')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField(null=True)),
                ('spoiler', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_users', models.ManyToManyField(related_name='like_rating', to=settings.AUTH_USER_MODEL)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movies.movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='characters',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters_id', to='movies.movie'),
        ),
    ]
