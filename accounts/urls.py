from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
    url(r'^signup/$', views.register_form, name = 'register'),
    )

