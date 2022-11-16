<<<<<<< Updated upstream
# Generated by Django 3.2.11 on 2022-11-16 07:19
=======
# Generated by Django 3.2.11 on 2022-11-16 07:15
>>>>>>> Stashed changes

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audlt', models.BooleanField()),
                ('backdrop_path', models.CharField(max_length=200)),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('poster_path', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('runtime', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('vote_average', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
