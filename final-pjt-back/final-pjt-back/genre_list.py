import requests
import json
from pprint import pprint 


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


maker = URLMaker('f0d4ab509782989d8df374a0bef09983')
# print(maker.get_url('genre', 'movie/list', region='KR', language='ko'))

genre_url = maker.get_url('genre', 'movie/list', region='KR', language='ko')

try:
    response = requests.get(genre_url)
    res_data = json.loads(response.text)
    genres = []
    for i in range(len(res_data['genres'])):
        genre_id = res_data['genres'][i]['id']
        genre_name = res_data['genres'][i]['name']

        genre_info_dict = {
            'model' : 'movies.genre',
            'pk' : i+1,
            'fields' : {
                'genre_id' : genre_id,
                'genre_name' : genre_name
            }
        }
        genres.append(genre_info_dict)

        with open('genres.json', 'w', encoding='UTF8') as f:
            json.dump(genres, f, ensure_ascii = False)
except:
    print('오류났음!')

