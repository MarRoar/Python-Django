from django.conf.urls import url
from . import views

# app_name = 'summary'
urlpatterns = [
    url(r'^$', views.index)
]