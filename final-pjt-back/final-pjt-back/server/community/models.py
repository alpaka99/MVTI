from django.db import models
from django.db.models.deletion import CASCADE
# from django.apps import apps
from django.conf import settings
from django.db.models.fields import IntegerField
# Create your models here.

# Movie = apps.get_model('movies', 'Movie')

class Review(models.Model):
    # 유저랑 연결
    # # 유저는 모델 그냥 넣으면 안돼
    # # #  user.object.review_set  으로 하면 원래 전부 다 불러올 수 있음 (역참조)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    # 영화랑 연결
    # movie.object.movie_set (역참조)
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    # 여기에 평점 가져오는건 어떻게 하지?

    title = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField() # 평점
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)


class Comment(models.Model):

    # 유저랑 연결
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    # 리뷰랑 연결
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()

    