from django.shortcuts import render
from django.http import HttpResponse
from .models import User
import json
# Create your views here.
def login(request):
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    print(body_data)
    result = User.objects.filter(uname=body_data['uname'],upwd=body_data['upwd'])
    if result.count()>0:
        return HttpResponse(json.dumps({"code":1,'msg':'login success'}))
    else:
        return HttpResponse(json.dumps({"code":0,'msg':'login failed'}))
def register(request):
    print(type(request.body))
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    # 检查用户名是否可用
    result = User.objects.filter(uname=body_data['uname'])
    if result.count()==0:
        # 如果可用 插入到数据库中
        newUser = User(uname=body_data['uname'],upwd=body_data['upwd'])
        newUser.save()  
        return HttpResponse(json.dumps({"code":1,"msg":'register success'}))
    else:
        return HttpResponse(json.dumps({"code":0,"msg":'register failed 用户名已经存在'}))    
    
