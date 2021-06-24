import requests
import json
from pprint import pprint 

url = "https://api.themoviedb.org/3/movie/top_rated?api_key=f0d4ab509782989d8df374a0bef09983&language=ko-KR&page=1"
apikey = "f0d4ab509782989d8df374a0bef09983"

response = requests.get(url)

# print(response)
# print(dir(response))
# print(response.text)
# print(type(response.text)) # <class 'str'> # json은 파이썬 내부에서 dict과 비슷하게 생겼음에도 그냥 사용 못함!
# print(response.json())
# print(type(response.json())) #<class 'dict'>

# movie_dict = response.json() # dict로 변환

# pprint(movie_dict)

class URLMaker():
    # 기본url 
    base_url = "https://api.themoviedb.org/3"
    
    # 생성할때 apikey 넣었음
    def __init__(self, key):
        self.key = key
    
    # 영화 url
    def get_url(self, category, feature, **kwargs):
        url = f'{URLMaker.base_url}/{category}/{feature}'
        url += f'?api_key={self.key}'
        for k, v in kwargs.items():
            url += f'&{k}={v}'
        return url

    # 영화 검색
    def movie_id(self, title):
        # /search/movie
        url=self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)
        # print(res.text) #json(class str)
        # print(type(res.json()))
        movie_dict = res.json()


maker = URLMaker('f0d4ab509782989d8df374a0bef09983')
# print(maker.key)
# print(maker.get_url('movie', 'top_rated', region='KR'))
# print(maker.get_url('genre', 'movie/list', region='KR', language='ko'))
# maker.movie_id('기생충')


