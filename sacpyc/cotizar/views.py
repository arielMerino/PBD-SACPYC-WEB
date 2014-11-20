# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView

#def home(request):
#	context={'dicc1':'valor dicc 1'}
#	return render(request,'sd/home.html',context)

class Cotizar(TemplateView):
	def __init__(self, valor):		
		self.valor = valor
	def cotizar(self, request):
		context = {'valor1':'','valor2':'','valor3':''}
		return render(request, 'cotizar/cotizar.html',context)
