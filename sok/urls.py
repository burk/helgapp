from django.conf.urls import patterns, url

from sok import views

urlpatterns = patterns('',
    url(r'^apply/$', views.apply, name = 'apply'),
    url(r'^applications/$', views.applications, name = 'applications'),
    )

