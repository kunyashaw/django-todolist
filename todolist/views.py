from django.shortcuts import render
from django.http import HttpResponse

from todolist.models import Item
import json
from django.core import serializers


# Create your views here.
def index(request):
    return HttpResponse("Hello World")
def list(request):
    list = Item.objects.all()
    # list = Item.objects.only('content','done')
    print(list)
    tmpList=[]
    for tmp in list:
        tmpList.append({'content':tmp.content,'done':tmp.done,'id':tmp.id})
    # data = serializers.serialize("json", list)
    return HttpResponse(json.dumps({"data": tmpList}), content_type='application/json')
    # return HttpResponse(list)
def add(request,content,done):
    newItem = Item(content=content,done=done)
    newItem.save()
    return HttpResponse('add success')
def modify(request,id,done):
    myItem = Item.objects.get(id=id)
    myItem.done = done
    myItem.save()
    return HttpResponse('modify success')
