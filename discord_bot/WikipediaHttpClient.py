import requests
import urls
from WikiResponse import WikiSearchResponse
from dataclasses import dataclass


HTTP_OK = 200


def search(query) -> WikiSearchResponse:
    params = {'namespace': 0, 'format': 'json', 'search': query}
    try:
        request = requests.get(
            urls.wikipedia_open_search, params=params)
        if request.status_code == HTTP_OK:
            json = request.json()
            return WikiSearchResponse(json[0], json[1], json[3], request.status_code)
        else:
            return WikiSearchResponse.empty(request.status_code)
    except Exception as e:
        return WikiSearchResponse.empty(e)


def get_summary(article_title) -> str:
    params = {'titles': article_title, 'format': 'json'}
    request = requests.get(urls.wikipedia_summary, params=params)
    if request.status_code == HTTP_OK:
        json = request.json()['query']
        resp = list(json['pages'].values())[0]
        return resp.get('extract', '')
    return 'Article not found'
