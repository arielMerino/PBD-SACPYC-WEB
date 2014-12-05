from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import Home

urlpatterns = [
    url(r'^admin_django/', include(admin.site.urls)),
    url(r'^$',Home(0).inicio),
    url(r'^Cotizar/', include('Cotizar.urls')),
    url(r'^Contacto/',include('contacto.urls')),
    url(r'^Agenda/',include('Agenda.urls')),
    url(r'^Compras/',include('Compras.urls')),
    url(r'^Garzones/',include('Garzones.urls')),
    url(r'^CotizarAd/',include('CotizarAd.urls')),
    url(r'^TipoEvento/',include('TipoEvento.urls')),
    url(r'^Proveedores/',include('Proveedores.urls')),
    url(r'^Notificaciones/',include('Notificaciones.urls')),
    url(r'^Menu/',include('Menu.urls')),
]
