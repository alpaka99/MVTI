# Generated by Django 3.2.3 on 2021-05-25 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.IntegerField()),
                ('genre_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviedb_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('poster_path', models.TextField()),
                ('backdrop_path', models.TextField()),
                ('overview', models.TextField()),
                ('release_date', models.TextField()),
                ('vote_average', models.DecimalField(decimal_places=1, max_digits=10)),
                ('vote_count', models.IntegerField()),
                ('popularity', models.DecimalField(decimal_places=3, max_digits=10)),
                ('genre_ids', models.TextField()),
            ],
        ),
    ]