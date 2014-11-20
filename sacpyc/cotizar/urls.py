# -*- encoding: utf-8 -*-home
from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import Cotizar

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    
    #url(r'^$','sd.views.home',name='home'), #pagina principal
    url(r'^cotizar/$',Cotizar(0).cotizar)
)