from django.urls import path
from . import views

# 앱네임?
# 로그인은 json webtoken 쓸거라 안해도 됨
urlpatterns = [
    # accounts/~  post 회원가입
    path('signup/', views.signup),

    # accounts/user_pk/ 회원 정보 -> GET 조회
    path('<int:user_pk>/', views.profile),
    


    #
    path('user/', views.user_update_delete)
]
