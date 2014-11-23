from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import Home

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',Home(0).inicio),
    url(r'^Cotizar/', include('Cotizar.urls')),
)