from django.conf.urls import patterns, url

from flort import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

