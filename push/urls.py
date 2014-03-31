from django.conf.urls import patterns, url

from push import views

urlpatterns = patterns('',
    url(r'^auth$', views.auth, name='auth'),
    url(r'^m/(?P<channel>[\w-]+)$', views.message, name='message'),
)
