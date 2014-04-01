from django.conf.urls import patterns, include, url

from django.contrib import admin

from backend import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^pusher/', include('push.urls')),
    url(r'^(?P<channel>[\w-]+)?$', views.home, name='channel'),
)
