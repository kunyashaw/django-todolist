from django.shortcuts import render,get_object_or_404
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
    return HttpResponse(json.dumps({'code':1,"data": tmpList}), content_type='application/json')
    # return HttpResponse(list)
def add(request,content):
    newItem = Item(content=content,done=0)
    newItem.save()
    print(newItem.id)
    return HttpResponse(json.dumps({"code": 1,"id":newItem.id}), content_type='application/json')

def modify(request,id,done):
    # myItem = get_object_or_404(Item,id=id)
    try:
        myItem = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return HttpResponse(json.dumps({"code":0,"msg":"modify failed"}))    
    myItem.done = done 
    myItem.save()
    # myItem之所以可以转字符串，是因为已经在订制过Item这个类，加了个str
    return HttpResponse(json.dumps({"code":1,"msg":"modify success"}))
def delete(request,id):
    # 解决方案1：直接找，但是有可能不存在
    # obj = Item.objects.get(id=id)
    # 解决方案2：使用404方案，找不到就直接返回用户404
    # obj = get_object_or_404(Item,id=id)
    # 解决方案3：自己捕获异常
    try:
        obj = Item.objects.get(id=id)
    except Item.DoesNotExist:
        obj = None
        return HttpResponse(json.dumps({"code":0,"msg":"del failed,item does not exist"}))
    obj.delete()
    return HttpResponse(json.dumps({"code":1,"msg":"del success"}))

