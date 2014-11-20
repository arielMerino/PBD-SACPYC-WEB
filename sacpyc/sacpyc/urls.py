# -*- encoding: utf-8 -*-home
from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import Home

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    
    #url(r'^$','sd.views.home',name='home'), #pagina principal
    url(r'^$',Home(0).home),
    url(r'^cotizar/$',include('cotizar.urls')),
    url(r'^contactos/$',include('contactos.urls')),
    url(r'^admin/', include(admin.site.urls))
)