from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls \
  import staticfiles_urlpatterns 


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^', include("blog.urls", namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns += staticfiles_urlpatterns()

# At the top of your urls.py file, add the following line:


# UNDERNEATH your urlpatterns definition, add the following two lines:
## if settings.DEBUG:
##     urlpatterns += patterns(
##         'django.views.static',
##         (r'media/(?P<path>.*)',
##         'serve',
##         {'document_root': settings.MEDIA_ROOT}), )
