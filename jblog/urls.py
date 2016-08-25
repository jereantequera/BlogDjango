from django.conf.urls import patterns, include, url
from jblog.models import *
from jblog.views import post


urlpatterns = [
       url(r'^post/(?P<id_post>\d+)$', 
       post, 
       name='post'),
   url(r'^$', "jblog.views.main"),
]
