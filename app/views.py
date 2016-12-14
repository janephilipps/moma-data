import csv
import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Artist

def index(request):
    return render_to_response('index.html')

artists = Artist.objects.all()

def get_genders(artists):

    male = 0
    female = 0

    for a in artists:
        if a.gender == 'M':
            male += 1
        elif a.gender == 'F':
            female += 1

    return {'gender': [{'label': 'male', 'count': male},{'label':'female', 'count': female}]}

response = get_genders(artists)

def api(request):
    return HttpResponse(json.dumps(response), content_type='application.json')
