"""
Definition of views.
"""

from django.http import HttpRequest,HttpResponse,JsonResponse
from app import UrlShortStatic
from app import UrlShortener as US
import json

urlshort = US.UrlShortener()
def shorts(request):
    response = JsonResponse({'Error 500':'Link Not Found'})
    try:
        assert isinstance(request, HttpRequest)
        path = request.path
        if len(path) == UrlShortStatic.shortLength + 2:
            path = path[1:UrlShortStatic.shortLength + 1]
            response = HttpResponse(urlshort.getRedirect(path))
    finally:
        return response

def error(request):
    assert isinstance(request, HttpRequest)
    return JsonResponse({'Error 404':request.path})

def shorten_url(request):
    assert isinstance(request, HttpRequest)
    response = JsonResponse({'Error 500':'Request Error'})
    try:
        if request.method == 'POST':
            json_data = json.loads(request.body)
            url=json_data['url'] 
            short = urlshort.addUrl(url)
            response = JsonResponse({'shortened_url':request._current_scheme_host+'/'+ short})
    finally:
        return response
