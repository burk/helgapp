from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helgapp.views.home', name='home'),
    # url(r'^helgapp/', include('helgapp.foo.urls')),

    # Landingpage
    url(r'', include('landingpage.urls')),
    #url(r'flort', include('flort.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^sok/', include('sok.urls')),
    url(r'^snapp/', include('snapp.urls')),
)
