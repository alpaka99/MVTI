from django.urls import path
from . import views

# 앱네임?

urlpatterns = [
    # ~ community/
    # GET, POST => 리뷰 전체 조회 혹은 생성
    path('', views.reviews_list_create),

    # community/<review_pk>/ GET, PUT, DELETE => 리뷰 조회, 수정, 삭제
    path('<int:review_pk>/', views.review_detail_put_delete),


    # community/<review_pk>/comments/ GET, POST=> 리뷰의 댓글 조회 작성
    path('<int:review_pk>/comments/', views.comment_list_create),

    
    # community/comments/<comment_pk> => 댓글 수정 삭제
    path('comments/<int:comment_pk>/', views.comment_put_delete),
    


]
