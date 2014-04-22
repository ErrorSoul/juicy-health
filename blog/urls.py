#coding: utf:8
from django.conf.urls import patterns, url
from blog.views import Posts, PostDetailView

urlpatterns = patterns('',
                url(r'^$', Posts.as_view(), name="index"),
                url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view()),
         )
