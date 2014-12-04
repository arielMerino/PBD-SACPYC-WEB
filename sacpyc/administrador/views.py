# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView
from django.template import RequestContext

class Administrador(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaAdmin(self,request):
		return render(request,'administrador/administrador.html',self.context)