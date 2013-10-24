from django.conf.urls import patterns, url

from snapp import views

urlpatterns = patterns('',
    url(r'^rate/$', views.rate, name = 'rate_snap'),
    )

