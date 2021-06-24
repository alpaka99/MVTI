
# api 키 필요
# 내 api 
# f0d4ab509782989d8df374a0bef09983

# 예제
# https://api.themoviedb.org/3/movie/76341?api_key=f0d4ab509782989d8df374a0bef09983


# https://api.themoviedb.org/3/movie/popular?api_key=f0d4ab509782989d8df374a0bef09983&language=ko-KR&page=1

# base url
# https://api.themoviedb.org/3/

# import urllib.parse as par
# import urllib.parse as req

# # 영화 
# url = 

# import requests


# class URLMaker:    
#     url = 'https://api.themoviedb.org/3'

#     def __init__(self, key):
#         self.key = key

#     def get_url(self, category='movie', feature='popular', **kwargs):
#         url = f'{self.url}/{category}/{feature}'
#         url += f'?api_key={self.key}'

#         for k, v in kwargs.items():
#             url += f'&{k}={v}'

#         return url
        

#     def movie_id(self, title):
#         url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
#         res = requests.get(url)
#         movie = res.json()

#         if len(movie.get('results')):
#             return movie.get('results')[0].get('id')
#         else:
#             return None
    


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

# 정보를 알고 싶은 영화 리스트 만들기
movie_list = range(501, 502)


# API 지정

api = "https://api.themoviedb.org/3/movie/{movies}?api_key={key}&language=ko-KR"



# string.format_map() 매핑용 클래스 만들기

class Default(dict):
    def __missing__(self, key):
        return key



# 각 영화의 정보 추출하기

for name in movie_list:
    try:
        # API의 URL 구성하기
        url = api.format_map(Default(movies=name, key=apikey))
        print(url)  # 데이터 확인

        # API에 요청을 보내 데이터 추출하기
        r = requests.get(url)  # json 형태의 데이터가 나온다.
        # print(type(r))  # <class 'requests.models.Response'>

        # 결과를 JSON 형식으로 변환하기
        data = json.loads(r.text)
        # print(type(data))  # <class 'dict'>
        print(data)  # 데이터 확인
        print("+ 영화제목 =", data["title"])
        print("| 장르 =", data["genres"][0]["name"])
        print("| 원본 제목 =", data["original_title"])
        print("| 개요 =", data["overview"])
        print("| 유명도 =", data["popularity"])
        print("| 제작사 =", data["production_companies"][0]["name"])
        print("")

    except:
        pass
        print("영화번호 " + name + " 에 데이터 없음")