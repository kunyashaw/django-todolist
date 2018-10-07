from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    return HttpResponse('hello store')
def pList(request):
    list=[1,2,3,4,5]
    template = loader.get_template('store/list.html')
    context = {
        'latest_question_list': list,
    }
    return HttpResponse(template.render(context, request))