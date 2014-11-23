# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView

#def home(request):
#	context={'dicc1':'valor dicc 1'}
#	return render(request,'sd/home.html',context)

class Home(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def inicio(self,request):
		return render(request,'sacpyc/home.html',self.context)
