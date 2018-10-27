from django.conf.urls import url
from . import views

app_name = 'modelslearn'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^testjson', views.testjson),
    url(r'^getTest', views.getTest),
    url(r'^getTest1', views.getTest1),
    url(r'^postTest1', views.postTest1),
    url(r'^postTest2', views.postTest2),
    url(r'^session1/$', views.session1),
    url(r'^session2/$', views.session2),
    url(r'^session2handle/$', views.session2handle),
    url(r'^session3/$', views.session3),
]
