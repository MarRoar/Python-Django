from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import BookInfoz
# Create your views here.


def index(request):
    # return HttpResponse("hello")
    booklist = BookInfo.objects.all()
    template = loader.get_template('summary/index.html')
    context = RequestContext(request, {'booklist': booklist})
    return HttpResponse(template.render(context))