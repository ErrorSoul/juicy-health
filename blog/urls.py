#coding: utf:8
from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
                url(r'^$', views.Posts.as_view(), name="index"),
                url(r'^post/(?P<pk>\d+)/$',
                    views.PostDetailView.as_view(), name="pt_detail"),
         )
