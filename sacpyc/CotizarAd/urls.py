from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import CotizarAd

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Presentacion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^CotizarAd/$', CotizarAd("a").llamadaCotizarAd)
)