import csv
import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Artist

def index(request):
    return render_to_response('index.html')

# Prepare API response
artists = Artist.objects.all()

# JSON
# { gender: [
#     {'Male': 100 },
#     {'Female': 10}
#   ]
# }


def get_genders(artists):

    data = dict()
    gender = []
    male = 0
    female = 0

    for a in Artist.objects.all():
        if a.gender == 'M':
            male += 1
        elif a.gender == 'F':
            female += 1

    print('M', male)
    print('F', female)

    gender.setdefault('male',list()).append(male)
    gender.setdefault('female',list()).append(female)

    data.setdefault('gender',dict()).append(gender)

    return data

response = get_genders(artists)

# TODO: update to relative path/find where to put csv file
# with open('/Users/janephilipps/code/moma-data/app/artist-gender-data.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         response.append(row)

def api(request):
    return HttpResponse(json.dumps(response), content_type='application.json')
