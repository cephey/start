# coding: utf-8

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'', include('pages.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
