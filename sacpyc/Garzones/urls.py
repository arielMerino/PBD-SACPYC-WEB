from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import Garzones

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Presentacion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^Garzones/$', Garzones("a").llamadaGarzones)
)