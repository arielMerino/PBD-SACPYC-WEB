from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import Home

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$','sd.views.home',name='home'), #pagina principal
    url(r'^$',Home.as_view()),
    url(r'^Cotizar/', include('Cotizar.urls')),
)