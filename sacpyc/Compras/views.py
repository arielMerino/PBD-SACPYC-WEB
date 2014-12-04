# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView
from django.template import RequestContext

class Compras(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaCompras(self,request):
		return render(request,'compras/compras.html',self.context)