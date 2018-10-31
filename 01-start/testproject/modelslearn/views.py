from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .models import BookInfo, HeroInfo
from django.db.models import Max,F,Q
import json
# Create your views here.

def index(request):

    # b = BookInfo.objects.all() # 查询所有的
    # 字段名字__contains
    # b = BookInfo.objects.filter(btitle__contains="经") # 查询btitle 包含有 经 的
    # b = BookInfo.objects.filter(pk__in=[1])
    b = BookInfo.objects.all()

    booklist = {
        'booklist': b
    }
    return render(request, 'modelslearn/index.html', booklist)

def testjson(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")

def getTest(request):
    resp = {
        'path': request.path,
        'method': request.method,
        'encoding': request.encoding,
        'method': request.method,
        'COOKIES': request.COOKIES,
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")
# 测试get
def getTest1(request):
    # a = request.GET['a']
    a = request.GET.getlist('a') # 如果有多个值的话用getlist来接收
    b = request.GET['b']
    resp = {
        'a': a,
        'b': b
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

# 测试 post
def postTest1(request):
    return render(request, 'modelslearn/postTest1.html')

def postTest2(request):
    resp = {
        "uname": request.POST['uname'],
        "upwd": request.POST['upwd'],
        "ugender": request.POST['ugender'],
        "uhobby": request.POST.getlist('uhobby'),
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


def session1(request):
    uname = request.session.get('myname', '未登录')
    content = {
        'uname': uname
    }
    return render(request, 'modelslearn/session1.html', content)

def session2(request):
    return render(request, 'modelslearn/session2.html')

def session2handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    return redirect('/session1/')

def session3(request):
    del request.session['myname']
    return redirect('/session1/')