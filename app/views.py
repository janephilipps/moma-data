import csv
import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('index.html')

# Prepare API response
response = []

# TODO: update to relative path/find where to put csv file
with open('/Users/janephilipps/code/moma-data/app/artist-gender-data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        response.append(row)

def api(request):
    return HttpResponse(json.dumps(response), content_type='application.json')
