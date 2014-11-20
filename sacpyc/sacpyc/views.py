# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView

#def home(request):
#	context={'dicc1':'valor dicc 1'}
#	return render(request,'sd/home.html',context)

class Home(TemplateView):
	template_name = "sacpyc/home.html"
