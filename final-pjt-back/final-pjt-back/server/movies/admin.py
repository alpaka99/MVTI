from django.contrib import admin
from .models import Movie

# Register your models here.


# 관리자 페이지에서 예쁘게 보이도록 설정
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'overview', 'poster_path',)


admin.site.register(Movie, MovieAdmin)
# admin.site.register(Movie,)
