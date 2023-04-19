import requests
import urls
from WikiResponse import WikiResponse

default_params = {'namespace': 0, 'format': 'json', 'search': ''}
SEARCH = 'search'
HTTP_OK = 200


def make_wikipedia_request(query) -> WikiResponse:
    try:
        default_params[SEARCH] = query
        request = requests.get(urls.wikipedia_open_search, params=default_params)
        if request.status_code == HTTP_OK:
            json = request.json()
            return WikiResponse(json[0], json[1], json[3], request.status_code)
        else:
            return WikiResponse.empty(request.status_code)
    except Exception as e:
        return WikiResponse.empty(e)
