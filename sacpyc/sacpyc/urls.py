from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import Home

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',Home(0).inicio),
    url(r'^Cotizar/', include('Cotizar.urls')),
<<<<<<< HEAD
]
=======
    url(r'^Contacto/',include('contacto.urls')),
)
>>>>>>> 09615b6da887e233d12d329111f6da31cb2d2a8f
