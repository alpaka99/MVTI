from django.urls import path
from . import views

# 앱네임?

urlpatterns = [
    # movies/ GET : 영화 전체 목록 불러오기 -> 전체 어떻게?
    path('', views.movies_list),
    # movie/movie_id/, GET : 해당 영화 정보 불러오기, 
    path('<int:movie_pk>/', views.movie_detail),

    # movie/recommend/genre_id post -> 데이터 넘어옴
    path('recommend/', views.movie_recommend)

]
