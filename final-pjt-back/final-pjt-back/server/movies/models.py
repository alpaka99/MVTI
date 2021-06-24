from django.db import models

# Create your models here.

class Movie(models.Model):
    # 리뷰 연결하기

    moviedb_id = models.IntegerField()
    title = models.CharField(max_length=100) # max_length 필수
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    overview = models.TextField()
    release_date= models.TextField()
    vote_average = models.DecimalField(max_digits=10, decimal_places=1)
    vote_count = models.IntegerField()
    popularity= models.DecimalField(max_digits=10, decimal_places=3)
    genre_ids = models.TextField()

    # def __str__(self):
    #     return self.overview


class Genre(models.Model):
    genre_id = models.IntegerField()
    genre_name = models.TextField()