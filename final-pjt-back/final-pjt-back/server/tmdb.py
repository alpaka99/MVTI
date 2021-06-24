# 영화정보를 API를 이용해서 가져오기

# 홈페이지  https://www.themoviedb.org/

# Document  https://developers.themoviedb.org/3

import requests
import json
# API 지정
apikey = "f0d4ab509782989d8df374a0bef09983"


################
#  GET RATED   #
################

# 정보를 알고 싶은 영화 페이지 리스트
page_list = range(1, 6)

# API 지정
api = "https://api.themoviedb.org/3/movie/top_rated?api_key={key}&language=ko-KR&page={page}"



# string.format_map() 매핑용 클래스 만들기

class Default(dict):
    def __missing__(self, key):
        return key



# 각 영화의 정보 추출하기

movies = []
for page in page_list:
    try:
        # API의 URL 구성하기
        url = api.format_map(Default(page=page, key=apikey))
        # 데이터 확인
        print(url)  
        # API에 요청을 보내 데이터 추출하기
        r = requests.get(url)  # json 형태의 데이터가 나온다.
        # 결과를 JSON 형식으로 변환하기
        data = json.loads(r.text) # <class 'dict'>
        
        for i in range(len(data['results'])):
            # print(data['results'][i])
            moviedb_id = data['results'][i]['id']
            title = data['results'][i]['title']
            poster_path = data['results'][i]['poster_path']
            backdrop_path = data['results'][i]['backdrop_path']
            overview = data['results'][i]['overview']
            release_date = data['results'][i]['release_date']
            vote_average = data['results'][i]['vote_average']
            vote_count = data['results'][i]['vote_count']
            popularity = data['results'][i]['popularity']
            genre_ids = data['results'][i]['genre_ids']

            movie_info_dict = {
                'model': 'movies.movie',
                'pk' : i+(page-1)*20,
                'fields': {
                    'moviedb_id' : moviedb_id,
                    'title' : title,
                    'poster_path' : poster_path,
                    'backdrop_path' : backdrop_path,
                    'overview' : overview,
                    'release_date' : release_date,
                    'vote_average' : vote_average,
                    'vote_count' : vote_count,
                    'popularity' : popularity,
                    'genre_ids' : genre_ids
                }
            }
            movies.append(movie_info_dict)
        

    except:
        print( page + " 에 데이터 없음")


with open('movies.json', 'w', encoding='UTF8') as json_file:
            json.dump(movies, json_file, ensure_ascii = False )
        