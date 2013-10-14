from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    )

