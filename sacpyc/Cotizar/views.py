# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView

#def home(request):
#	context={'dicc1':'valor dicc 1'}
#	return render(request,'sd/home.html',context)

class Cotizar(TemplateView):
	def __init__(self,valor): #cuando usas INIT, debes siempre inicializar todos tus objetos.
		self.valor = valor
	def llamadaCotizar(self,request):
		return render(request, 'Cotizar/cotizar.html', {})
