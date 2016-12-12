import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('index.html')

def api(request):
    return HttpResponse(json.dumps([
        { 'label': 'Male', 'count': 1000 },
        { 'label': 'Female', 'count': 100 }
    ]), content_type='application.json')
