from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from IdeaPublisher.models import Feedback, Idea
#from django.utils import json

class JSONResponse(HttpResponse):
    def __init__(self, data):
        super(JSONResponse, self).__init__(
                json.dumps(data), mimetype='application/json')

@csrf_exempt
def searchPublicacion(request):
    response = []
    if request.method == 'POST':
        response_data = {}
        response_data['msg'] = 'Post was deleted.'
        obj = Feedback.objects.filter(id=request.POST['id'])
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JsonResponse({"Nothing to see": "this isn't happening"})
		

@csrf_exempt
def searchCrzIdea(request):
    response = []
    if request.method == 'POST':
        response_data = {}
        response_data['msg'] = 'Post was deleted.'
        obj = Idea.objects.filter(id=request.POST['id'])
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JsonResponse({"Nothing to see": "this isn't happening"})		