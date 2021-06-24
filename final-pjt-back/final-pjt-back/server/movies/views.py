from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view


from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# DRF
# 1. api_view 라는 데코레이션 필수
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movies_list(request):
    if request.method == 'GET':
        # GET : 전체 영화 => JSON으로 넘겨야 => response 활용
        # data -> 'serializer'
        movies = Movie.objects.all()
        
        serializer = MovieListSerializer(movies, many=True)  #instance -> 직렬화 할 정보 인스턴스 ## many=True : 개발 철학상 여러개일때는 적어줘야
        return Response (serializer.data) # .data 해서 간편히 꺼낼 수 있음


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(requset, movie_pk):
    if requset.method=='GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_recommend(request):
    if request.method == 'POST':
        # print(request.data) # {'g0': [10749, 5], 'g1': [878, 6], 'g2': [80, 5], 'g3': [10752, 5]}
        user = request.user
        
        genres_list = [request.data['g0'][0], request.data['g1'][0], request.data['g2'][0], request.data['g3'][0]] 
        grades_list = [request.data['g0'][1], request.data['g1'][1], request.data['g2'][1], request.data['g3'][1]]
       
        myreviews = user.reviews.all()

        # 리뷰 순회하면서
        for myreview in myreviews:
            # MVTI 장르 순회
            for i in range(4):
                if str(genres_list[i]) in myreview.movie.genre_ids and myreview.rating >=8:
                    grades_list[i] +=1
                elif str(genres_list[i]) in myreview.movie.genre_ids and myreview.rating <=3:
                    grades_list[i] -=1
    
        # recommend_genre = genres_list[grades_list.index(max(grades_list))]
        # recommend_genre
        

          
        return Response({'장르' : genres_list, '점수' : grades_list}) 